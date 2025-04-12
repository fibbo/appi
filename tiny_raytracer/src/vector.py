import json
import math


class Vector:
    def __init__(self, *args):
        self.components = []
        for n in args:
            self.components.append(n)
        self.size = len(self.components)

    def __str__(self):
        return str(self.components)

    def __repr__(self):
        return self.__str__()

    @property
    def x(self):
        return self.components[0]

    @property
    def y(self):
        return self.components[1]

    @property
    def z(self):
        return self.components[2]

    def dot(self, rhs):
        scalar_product = 0
        assert self.size == rhs.size
        for i in range(self.size):
            scalar_product += self.components[i] * rhs.components[i]
        return scalar_product

    def norm(self):
        return math.sqrt(self[0] * self[0] + self[1] * self[1] + self[2] * self[2])

    # TODO: Implement normalize
    def normalize(self, length=1):
        assert self.size == 3
        return self / (length * self.norm())

    def cross(self, rhs):
        return Vector(
            self.y * rhs.z - self.z * rhs.y,
            self.z * rhs.x - self.x * rhs.z,
            self.x * rhs.y - self.y * rhs.x,
        )

    def __add__(self, rhs):
        new_vec = []
        for i in range(self.size):
            new_vec.append(self.components[i] + rhs.components[i])

        # *new_vec unpacks the list. So instead of Vector([1,2,3])
        # it calls Vector(1, 2, 3)
        return Vector(*new_vec)

    def __sub__(self, rhs):
        new_vec = []
        for i in range(self.size):
            new_vec.append(self.components[i] - rhs.components[i])

        # *new_vec unpacks the list. So instead of Vector([1,2,3])
        # it calls Vector(1, 2, 3)
        return Vector(*new_vec)

    def __truediv__(self, rhs):
        new_vec = []
        for i in range(self.size):
            new_vec.append(self.components[i] / rhs)

        return Vector(*new_vec)

    def __mul__(self, rhs):
        new_vec = []
        for i in range(self.size):
            new_vec.append(self.components[i] * rhs)

        return Vector(*new_vec)

    def __rmul__(self, rhs):
        return self * rhs

    def __neg__(self):
        return self * -1

    def __eq__(self, rhs):
        if self.size != rhs.size:
            return False
        for i in range(self.size):
            if self.components[i] != rhs.components[i]:
                return False
        return True

    def __getitem__(self, index):
        return self.components[index]

    def to_json(self):
        return json.dumps(self.components)


if __name__ == "__main__":
    vector = Vector(1, 2, 3, 4, 5)
    print("This is printed from vector.py")
    print(vector.x)
    print(vector[0])
