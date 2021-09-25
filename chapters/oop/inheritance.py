import math


class Shape:
    def area(self):
        raise NotImplementedError("Cannot calculate area of a general shape")

    def circumference(self):
        raise NotImplementedError(
            "Cannot calculate the circumference of a general shape."
        )

    def __str__(self):
        return "Shape Class"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    shapes = []
    shapes.append(Circle(3))
    shapes.append(Rectangle(3, 4))
    for shape in shapes:
        print(shape.area())
        print(shape.circumference())


shape = Shape()
print(shape)
