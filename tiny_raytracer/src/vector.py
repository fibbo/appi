import math


class Vector:
    def __init__(self, *args):
        self.components = []
        for i in args:
            self.components.append(i)
        self.size = len(self.components)

    def __str__(self):
        return str(self.components)

    def cross(self, rhs):
        assert self.size == 3 and rhs.size == 3
        return Vector(
            self[1] * rhs[2] - self[2] * rhs[1],
            self[2] * rhs[0] - self[0] * rhs[2],
            self[0] * rhs[1] - self[1] * rhs[0],
        )

    def __getitem__(self, index):
        assert self.size > index
        return self.components[index]

    def __neg__(self):
        return self * -1

    def __mul__(self, scalar):
        new_vec = []
        for i in range(self.size):
            new_vec.append(self.components[i] * scalar)
        return Vector(*new_vec)

    def __rmul__(self, scalar):
        return self * scalar

    def __sub__(self, other):
        new_vec = []
        assert self.size == other.size
        for i in range(self.size):
            new_vec.append(self.components[i] - other.components[i])
        return Vector(*new_vec)

    def __truediv__(self, scalar):
        new_vec = []
        for i in range(self.size):
            new_vec.append(self.components[i] / scalar)
        return Vector(*new_vec)

    def __add__(self, other):
        new_vec = []
        assert self.size == other.size
        for i in range(self.size):
            new_vec.append(self.components[i] + other.components[i])
        return Vector(*new_vec)

    def dot(self, other):
        scalar_product = 0
        assert self.size == other.size
        for i in range(self.size):
            scalar_product += self.components[i] * other.components[i]
        return scalar_product

    def norm(self):
        return math.sqrt(self[0] * self[0] + self[1] * self[1] + self[2] * self[2])

    def __eq__(self, other):
        if len(self.components) != other.size:
            return False
        for i in range(self.size):
            if self.components[i] != other.components[i]:
                return False
        return True

    def normalize(self, length=1):
        assert self.size == 3
        return self / (length * self.norm())
