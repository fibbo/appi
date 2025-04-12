import json

from scene_base import SceneBase
from vector import Vector


class Material(SceneBase):
    """
    Material which is used to calculate the color of a ray or the refraction
    has to be calculated.
    """

    def __init__(self, *args):
        material_dict = None
        if len(args) == 5:
            self.name = args[0]
            self.refractive_index = args[1]
            self.albedo = args[2]
            self.diffuse_color = args[3]
            self.specular_exponent = args[4]
            return

        if len(args) == 1 and isinstance(args[0], str):
            material_dict = json.loads(args[0])
        if len(args) == 1 and isinstance(args[0], dict):
            material_dict = args[0]

        self.name = material_dict["name"]
        self.refractive_index = material_dict["refractive_index"]
        self.albedo = Vector(material_dict["albedo"])
        self.diffuse_color = Vector(material_dict["diffuse_color"])
        self.specular_exponent = material_dict["specular_exponent"]

    def __str__(self):
        return f"{self.name} - refractive index: {self.refractive_index}, albedo: {self.albedo}, diffuse color: {self.diffuse_color}, specular exponent: {self.specular_exponent}"

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.specular_exponent == other.specular_exponent
            and self.albedo == other.albedo
            and self.refractive_index == other.refractive_index
            and self.diffuse_color == other.diffuse_color
        )

    def to_json(self):
        material_dict = {
            "name": self.name,
            "refractive_index": self.refractive_index,
            "albedo": self.albedo.to_json(),
            "diffuse_color": self.diffuse_color.to_json(),
            "specular_exponent": self.specular_exponent,
        }
        return json.dumps(material_dict)
