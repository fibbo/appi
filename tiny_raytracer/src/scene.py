import json

from light import Light
from scene_base import SceneBase
from sphere import Sphere


class Scene(SceneBase):
    """
    Scene class. Contains the information of the scene such as Lights and Spheres
    """

    def __init__(self, lights=[], spheres=[]):
        self.lights = lights
        self.spheres = spheres

    def __getitem__(self, name):
        if name == "lights":
            return self.lights
        if name == "spheres":
            return self.spheres

    def __str__(self):
        output = ""
        for light in self.lights:
            output += light.__str__() + "\n"
        for sphere in self.spheres:
            output += sphere.__str__() + "\n"
        return output

    def to_json(self):
        scene_dict = {"lights": [], "spheres": []}
        for light in self.lights:
            scene_dict["lights"].append(light.to_json())
        for sphere in self.spheres:
            scene_dict["spheres"].append(sphere.to_json())

        return json.dumps(scene_dict)

    def from_json(self, json_string):
        scene_dict = json.loads(json_string)
        if "lights" in scene_dict:
            for light in scene_dict["lights"]:
                self.lights.append(Light(light))
        if "spheres" in scene_dict:
            for sphere in scene_dict["spheres"]:
                self.spheres.append(Sphere(sphere))
