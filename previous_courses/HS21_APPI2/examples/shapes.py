import math


class Shape:
    def area(self):
        print("Shape is an abstract class. It does not have an area.")

    def circumference(self):
        print(
            "Shape is an abstract class. It does not have a concept of circumference."
        )


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.width + self.height)


shape = Shape()
shape.area()
shape.circumference()

circle = Circle(1.0)
print(circle.area())
print(circle.circumference())

rectangle = Rectangle(2, 3)
print(rectangle.area())
print(rectangle.circumference())
