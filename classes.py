from math import pi
class Point:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Figure:
    pass

class Circle(Figure):
    def __init__(self, x, y,  radius):
        self.coord_of_cenntre = Point(coord_x=x,coord_y=y)
        self.radius = radius

    def perimetr(self, pi = 3.14):
        result_1_1 = 2 * pi * self.radius
        return result_1_1

    def square(self):
        result_1_2 = 3.14 * (self.radius**2)
        return result_1_2

class Triangle(Figure):
    def __init__(self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c


    def perimetr(self):
        result_2_1 = self.a + self.b + self.c
        return result_2_1

    def square(self):
        result_2_2 = 0.5 * (self.a + self.b)
        return result_2_2

class Square(Figure):
    def __init__(self, d):
        self.d = d

    def perimetr(self):
        result_3_1 = self.d * 4
        return result_3_1

    def square(self):
        result_3_2 = self.d ** 2
        return result_3_2



