from Classes.Geometry.Point import *


class Triangle:
    def __init__(self, first: Point, second: Point, third: Point):
        self.first = first
        self.second = second
        self.third = third

    def __str__(self):
        res = f"Треугольник с вершинами в точках:\n1) x={self.first.x} y={self.first.y}" \
              f"\n2) x={self.second.x} y={self.second.y}" \
              f"\n3) x={self.third.x} y={self.third.y}"
        return res

    def sides(self):
        side1 = distance(self.first, self.second)
        side2 = distance(self.second, self.third)
        side3 = distance(self.first, self.third)
        return side1, side2, side3

    def perimeter(self):
        return sum([i for i in self.sides()])


def main():
    p1 = Point(5, 10)
    p2 = Point(25, 5)
    p3 = Point(10, 10)
    print(p1)
    trian = Triangle(p1, p2, p3)
    print(f"Стороны треугольника: {', '.join(str(side) for side in trian.sides())}")
    print(f"Периметр треугольника: {trian.perimeter()}")


if __name__ == '__main__':
    main()
