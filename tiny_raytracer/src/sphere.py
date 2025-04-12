import json

from material import Material
from scene_base import SceneBase
from vector import Vector


class Sphere(SceneBase):
    """
    Simplest scene object. Has a center, radius and material
    """

    def __init__(self, *args):
        if len(args) == 3:
            self.center = args[0]
            self.radius = args[1]
            self.material = args[2]
            return
        if len(args) == 1 and isinstance(args[0], str):
            sphere_dict = json.loads(args[0])
        if len(args) == 1 and isinstance(args[0], dict):
            sphere_dict = args[0]
        self.center = Vector(sphere_dict["center"])
        self.radius = sphere_dict["radius"]
        self.material = Material(sphere_dict["material"])

    def __str__(self):
        return f"Sphere - center: {self.center}, radius: {self.radius}, {self.material}"

    def to_json(self):
        sphere_dict = {
            "center": self.center.to_json(),
            "radius": self.radius,
            "material": self.material.to_json(),
        }
        return json.dumps(sphere_dict)
