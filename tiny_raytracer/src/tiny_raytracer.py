import math
import sys
from vector import Vector

float_max = sys.float_info.max


class Light:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity


class Material:
    def __init__(self, refrac_index, albedo, diffuse_color, specular_exponent):
        self.refractive_index = refrac_index
        self.albedo = albedo
        self.diffuse_color = diffuse_color
        self.specular_exponent = specular_exponent


class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material


def ray_sphere_intersect(origin, direction, sphere):
    l = sphere.center - origin
    tca = l.dot(direction)
    d2 = l.dot(l) - tca * tca
    if d2 > sphere.radius * sphere.radius:
        return (False, 0)
    thc = math.sqrt(sphere.radius * sphere.radius - d2)
    t0 = tca - thc
    t1 = tca + thc
    if t0 < 1e-3:
        t0 = t1
    if t0 < 1e-3:
        return (False, 0)

    return (True, t0)


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

    return (spheres_dist < 1000, hit, normal, material)


def cast_ray(origin, direction, spheres, lights, depth=0):

    if depth > 4:
        return Vector(0.2, 0.7, 0.8)
    has_hit, point, normal, material = scene_intersect(origin, direction, spheres)
    if not has_hit:
        return Vector(0.2, 0.7, 0.8)

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


def render(spheres, lights):
    width = 400
    height = 200
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
                spheres,
                lights,
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


def main():
    ivory = Material(1.0, Vector(0.6, 0.3, 0.1, 0.0), Vector(0.4, 0.4, 0.3), 50)
    glass = Material(1.5, Vector(0.0, 0.5, 0.1, 0.8), Vector(0.6, 0.7, 0.8), 125)
    red_rubber = Material(1.0, Vector(0.9, 0.1, 0.0, 0.0), Vector(0.3, 0.1, 0.1), 10)
    mirror = Material(1.0, Vector(0.0, 10.0, 0.8, 0.0), Vector(1.0, 1.0, 1.0), 1425)

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

    render(spheres, lights)


main()
