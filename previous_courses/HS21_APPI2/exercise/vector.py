import math


class Vector:
    def __init__(self, *args):
        self.components = args
        self.size = len(self.components)

    # TODO: Implement __str__

    @property
    def x(self):
        return self.components[0]

    @property
    def y(self):
        return self.components[1]

    @property
    def z(self):
        assert self.size >= 3
        return self.components[2]

    def dot(self, rhs):
        assert self.size == rhs.size
        dot_product = 0
        for i in range(self.size):
            dot_product += self.components[i] * rhs.components[i]
        return dot_product

    def norm(self):
        norm_ = 0
        for c in self.components:
            norm_ += c ** 2
        return math.sqrt(norm_)

    def normalize(self):
        return self / self.norm()

    def cross(self, rhs):
        assert self.size == 3 and rhs.size == 3
        return Vector(
            self.y * rhs.z - self.z * rhs.y,
            self.z * rhs.x - self.x * rhs.z,
            self.x * rhs.y - self.y * rhs.x,
        )

    def __add__(self, rhs):
        new_vec = []
        assert self.size == rhs.size
        for i in range(self.size):
            new_vec.append(self.components[i] + rhs.components[i])
        return Vector(*new_vec)

    def __sub__(self, rhs):
        new_vec = []
        assert self.size == rhs.size
        for i in range(self.size):
            new_vec.append(self.components[i] - rhs.components[i])
        return Vector(*new_vec)

    def __truediv__(self, divisor):
        new_vec = []
        for i in range(self.size):
            new_vec.append(self.components[i] / divisor)
        return Vector(*new_vec)

    def __mul__(self, scalar):
        new_vec = []
        for i in range(self.size):
            new_vec.append(self[i] * scalar)
        return Vector(*new_vec)

    def __rmul__(self, scalar):
        return self * scalar

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
        assert self.size > index
        return self.components[index]

    pass
