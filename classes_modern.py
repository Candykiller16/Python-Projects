import math
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
class Figure:
    def __init__(self, area=None, perimeter=None):
        self.area = area
        self.perimeter = perimeter


class Circle(Figure):
    def __init__(self, a,  radius):
        self.a = a
        self.radius = radius
        self.perimeter = 2 * 3.14 * self.radius
        self.area = 3.14 * (self.radius **2)

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = self.sides()[0]
        self.bc = self.sides()[1]
        self.ac = self.sides()[2]
        self.perimeter = self.ab + self.bc + self.ac
        self.area = (self.ab + self.bc) / 2

    def sides(self):
        x1 = self.a.x
        y1 = self.a.y
        x2 = self.b.x
        y2 = self.b.y
        x3 = self.c.x
        y3 = self.c.y

        ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        ac = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        return ab , bc , ac

class Square(Figure):

    def __init__(self, d, e):
        self.d = d
        self.e = e
        self.de = self.sides_1()[0]
        self.perimeter = self.de * 4
        self.area = self.de ** 2

    def sides_1(self):
        x1 = self.d.x
        y1 = self.d.y
        x2 = self.e.x
        y2 = self.e.y

        de = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return de



