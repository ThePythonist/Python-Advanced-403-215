import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):  # mohit
        return self.radius * 2 * math.pi

    def area(self):  # masahat
        return self.radius * self.radius * math.pi


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width


def p_area(shape):  # polymorphic
    print("Area :", shape.area())


def p_perimeter(shape):  # polymorphic
    print("Perimeter :", shape.perimeter())


shape1 = Rectangle(2, 4)
shape2 = Circle(4)

# Calling Polymorphic Methods

p_area(shape2)
p_perimeter(shape2)
