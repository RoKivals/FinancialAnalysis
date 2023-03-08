from Point import *


class Rect:
    def __init__(self, first: Point, second: Point):
        self.first = first
        self.second = second

    def __str__(self):
        res = f"Прямоугольник с вершинами:\nЛевая верхняя: x={self.first.x} y={self.first.y}" \
              f"\nПравая нижняя: x={self.second.x} y={self.second.y}"
        return res

    def sides(self):
        side1 = abs(self.first.x - self.second.x)
        side2 = abs(self.first.y - self.second.y)
        return side1, side2

    def perimeter(self):
        return sum([i * 2 for i in self.sides()])


def main():
    p1 = Point(5, 10)
    p2 = Point(25, 5)
    print(p1)
    print(p2)
    rect = Rect(p1, p2)
    print(f"Стороны прямоугольника: {', '.join(str(side) for side in rect.sides())}")
    print(f"Периметр прямугольника: {rect.perimeter()}")


if __name__ == '__main__':
    main()
