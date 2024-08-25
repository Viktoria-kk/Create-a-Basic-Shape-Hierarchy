import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return None

    def __str__(self):
        return f"Shape: {self.name}, Area: {self.area()}"
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):

        return math.pi * (self.radius ** 2)

def print_area(shape):
    print(f"{shape.name} has an area of {shape.area():.0f}")

# rectangle = Rectangle("Rectangle", 10, 20)
# circle = Circle("Circle", 5)
#
# print_area(rectangle)
# print_area(circle)