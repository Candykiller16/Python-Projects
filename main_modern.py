from classes_modern import *

a = Point(0, 0)
b = Point(4, 16)
c = Point(4, 0)
d = Point(0, 0)
e = Point(0, 4)
f = Point(0, 0)

def main():
    circle = Circle(f, 5)
    triangle = Triangle(a, b, c)
    square = Square(d, e)
    new = []
    new.append(square.area)
    new.append(circle.area)
    new.append(triangle.area)
    print(new)


if __name__ == '__main__':
    main()