import math
import sys

from light import Light
from material import Material
from scene import Scene
from sphere import Sphere
from vector import Vector

float_max = sys.float_info.max


def ray_sphere_intersect(ray_origin, ray_direction, sphere):
    vector_to_sphere = sphere.center - ray_origin
    projection_length = vector_to_sphere.dot(ray_direction)
    perpendicular_distance_squared = (
        vector_to_sphere.dot(vector_to_sphere) - projection_length * projection_length
    )

    if perpendicular_distance_squared > sphere.radius * sphere.radius:
        return (False, 0)

    half_chord_length = math.sqrt(
        sphere.radius * sphere.radius - perpendicular_distance_squared
    )
    intersection_distance_1 = projection_length - half_chord_length
    intersection_distance_2 = projection_length + half_chord_length

    if intersection_distance_1 < 1e-3:
        intersection_distance_1 = intersection_distance_2

    if intersection_distance_1 < 1e-3:
        return (False, 0)

    return (True, intersection_distance_1)


def reflect(incoming, normal):
    return incoming - normal * 2.0 * (incoming.dot(normal))


def refract(incoming, normal, eta_t, eta_i=1.0):
    cosi = -max(-1.0, min(1.0, incoming.dot(normal)))
    if cosi < 0:
        return refract(incoming, -normal, eta_i, eta_t)
    eta = eta_i / eta_t
    k = 1 - eta * eta * (1 - cosi * cosi)
    if k < 0:
        return Vector(1, 0, 0)
    else:
        return incoming * eta + normal * (eta * cosi - math.sqrt(k))


def scene_intersect(origin, direction, spheres):
    spheres_dist = float_max
    hit = None
    normal = None
    material = None
    for sphere in spheres:
        res = ray_sphere_intersect(origin, direction, sphere)
        if res[0] and res[1] < spheres_dist:
            spheres_dist = res[1]
            hit = origin + direction * spheres_dist
            normal = (hit - sphere.center).normalize()
            material = sphere.material

    checkerboard_dist = float_max
    if abs(direction.y) > 1e-3:
        d = -(origin.y + 4) / direction.y
        pt = origin + direction * d
        if (
            d > 1e-3
            and abs(pt.x) < 10
            and pt.z < -10
            and pt.z > -30
            and d < spheres_dist
        ):
            checkerboard_dist = d
            hit = pt
            normal = Vector(0, 1, 0)
            diffuse_color = (
                Vector(0.3, 0.3, 0.3)
                if (int(0.5 * hit.x + 1000) + int(0.5 * hit.z)) & 1
                else Vector(0.3, 0.2, 0.1)
            )
            material = Material("checkerboard", 1, Vector(1, 0, 0, 0), diffuse_color, 0)

    return (min(spheres_dist, checkerboard_dist) < 1000, hit, normal, material)


def cast_ray(origin, direction, spheres, lights, depth=0):
    if depth > 4:
        return Vector(0.2, 0.7, 0.1)
    has_hit, point, normal, material = scene_intersect(origin, direction, spheres)
    if not has_hit:
        return Vector(0.2, 0.7, 0.1)

    reflect_dir = reflect(direction, normal).normalize()
    refract_dir = refract(direction, normal, material.refractive_index).normalize()
    reflect_color = cast_ray(point, reflect_dir, spheres, lights, depth + 1)
    refract_color = cast_ray(point, refract_dir, spheres, lights, depth + 1)

    diffuse_light_intensity = 0
    specular_light_intensity = 0
    for light in lights:
        light_dir = (light.position - point).normalize()

        has_hit, shadow_pt, _, _ = scene_intersect(point, light_dir, spheres)
        if has_hit and (shadow_pt - point).norm() < (light.position - point).norm():
            continue

        diffuse_light_intensity += light.intensity * max(0.0, light_dir.dot(normal))
        specular_light_intensity += (
            math.pow(
                max(0.0, -reflect(-light_dir, normal).dot(direction)),
                material.specular_exponent,
            )
            * light.intensity
        )
    return (
        material.diffuse_color * diffuse_light_intensity * material.albedo[0]
        + Vector(1.0, 1.0, 1.0) * specular_light_intensity * material.albedo[1]
        + reflect_color * material.albedo[2]
        + refract_color * material.albedo[3]
    )


def render(scene):
    width = 800
    height = 400
    # Change the width and height if you want a larger
    # or smaller image.
    fov = math.pi / 3.0
    framebuffer = width * height * [None]
    for j in range(height):
        for i in range(width):
            dir_x = (i + 0.5) - width / 2.0
            dir_y = -(j + 0.5) + height / 2.0
            dir_z = -height / (2.0 * math.tan(fov / 2.0))
            framebuffer[i + j * width] = cast_ray(
                Vector(0, 0, 0),
                Vector(dir_x, dir_y, dir_z).normalize(),
                scene["spheres"],
                scene["lights"],
            )

    with open("out.ppm", "wb") as f:
        f.write(bytearray(f"P6 {width} {height} 255\n", "ascii"))
        counter = 0
        for vec in framebuffer:
            counter += 1
            max_c = max(vec[0], max(vec[1], vec[2]))
            if max_c > 1:
                vec = vec * 1 / max_c
            vec = bytes([int(255 * vec[0]), int(255 * vec[1]), int(255 * vec[2])])
            f.write(vec)


def read_scene(url):
    lights = []
    spheres = []
    materials = {}

    answer = req.get(url)

    scene_object_type = None
    for line in answer.text.split("\n"):
        parts = line.split()
        if line == "":
            continue
        if line.startswith("#"):
            scene_object_type = parts[1]
        else:
            if scene_object_type == "materials":
                name = parts[0]
                refractive = float(parts[1])
                albedo = Vector(
                    float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5])
                )
                color = Vector(float(parts[6]), float(parts[7]), float(parts[8]))
                specular = float(parts[9])
                materials[name] = Material(name, refractive, albedo, color, specular)
            elif scene_object_type == "spheres":
                center = Vector(float(parts[0]), float(parts[1]), float(parts[2]))
                radius = float(parts[3])
                material = materials[parts[4]]
                spheres.append(Sphere(center, radius, material))
            elif scene_object_type == "lights":
                position = Vector(float(parts[0]), float(parts[1]), float(parts[2]))
                intensity = float(parts[3])
                lights.append(Light(position, intensity))


def write_scene_to_file(scene, file_name):
    with open(file_name, "w") as f:
        scene_string = scene.to_json()
        f.write(scene_string)


def load_scene_from_file(file_name):
    scene = Scene()
    with open(file_name, "r") as f:
        for line in f:
            scene.from_json(line)
            return scene


def main():
    ivory = Material(
        "ivory", 1.0, Vector(0.6, 0.3, 0.1, 0.0), Vector(0.4, 0.4, 0.3), 50
    )
    glass = Material(
        "glass", 1.5, Vector(0.0, 0.5, 0.1, 0.8), Vector(0.6, 0.7, 0.8), 125
    )
    red_rubber = Material(
        "red_rubber", 1.0, Vector(0.1, 0.4, 0.3, 0.0), Vector(0.3, 0.1, 0.1), 10
    )
    mirror = Material(
        "mirror", 1.0, Vector(0.0, 10.0, 0.8, 0.0), Vector(1.0, 1.0, 1.0), 1425
    )

    spheres = [
        Sphere(Vector(-3, 0, -16), 2, ivory),
        Sphere(Vector(-1.0, -1.5, -12), 2, glass),
        Sphere(Vector(1.5, -0.5, -18), 3, red_rubber),
        Sphere(
            Vector(
                7,
                5,
                -18,
            ),
            4,
            mirror,
        ),
    ]

    lights = [
        Light(Vector(-20, 20, 20), 1.5),
        Light(Vector(30, 50, -25), 1.8),
        Light(Vector(30, 20, 30), 1.7),
    ]
    scene = Scene(lights=lights, spheres=spheres)
    print(scene)
    render(scene)


if __name__ == "__main__":
    main()
