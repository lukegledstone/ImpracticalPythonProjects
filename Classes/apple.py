import math

class Apple():
    def __init__(self, colour, weight, taste, stem):
        self.colour = colour
        self.weight = weight
        self.taste = taste
        self.stem = stem



class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi

c1 = Circle(10)
print(c1.area())


class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

t1 = Triangle(10, 5)
print(t1.area())


class Hexagon():
    def __init__(self, length):
        self.length = length

    def calculate_perimeter(self):
        return self.length * 6

h1 = Hexagon(10)
print(h1.calculate_perimeter())