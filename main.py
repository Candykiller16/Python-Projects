from classes import *


def main():
    circle = Circle(5, 5, 5)
    triangle = Triangle(4, 4, 4)
    square = Square(2)
    figures = [circle, triangle, square]
    new = []
    for i in figures:
        new.append(i.square())
    print(new)


if __name__ == '__main__':
    main()