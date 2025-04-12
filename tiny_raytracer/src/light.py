import json

from scene_base import SceneBase
from vector import Vector


class Light(SceneBase):
    """
    Point light source with a position and an intensity (but not a color)
    """

    def __init__(self, *args):
        if len(args) == 2:
            self.position = args[0]
            self.intensity = args[1]
            return
        if len(args) == 1 and isinstance(args[0], str):
            light_dict = json.loads(args[0])
        elif len(args) == 1 and isinstance(args[0], dict):
            light_dict = args[0]

        self.intensity = light_dict["intensity"]
        self.position = Vector(*light_dict["position"])

    def __str__(self):
        return f"Light - position: {self.position} with intensity {self.intensity}"

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        light_dict = {"position": self.position.components, "intensity": self.intensity}
        return json.dumps(light_dict)

    def __eq__(self, other):
        return self.intensity == other.intensity and self.position == other.position
