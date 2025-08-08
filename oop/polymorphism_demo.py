import math


class Shape:
    def area(self):
        
        raise NotImplementedError("Subclasses must override the area() method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    shapes = [
        Rectangle(5, 3),
        Circle(4)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")