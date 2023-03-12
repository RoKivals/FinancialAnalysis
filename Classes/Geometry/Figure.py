from Point import *


class Figure:
    def __init__(self, point: Point):
        # Точка из фигуры (левый верхний угол)
        self.fir_point = point

    def draw(self, field=None):
        if field is None:
            field = [['.' for _ in range(40)] for _ in range(40)]
        for y in range(40):
            for x in range(40):
                if self.fir_point.x == x and self.fir_point.y == y:
                    field[y][x] = '*'
        return field

    @property
    def square(self):
        return 1

    def __str__(self):
        res = ''
        for i in self.draw():
            res = res + ''.join(x for x in i)
            res += '\n'
        return res


class Rectangle(Figure):
    def __init__(self, p1: Point, p2: Point):
        super().__init__(p1)
        # Правый нижний угол прямоугольника
        self.sec_point = p2

    def draw(self, field=None):
        if field is None:
            field = [['.' for _ in range(40)] for _ in range(40)]
        for y in range(40):
            for x in range(40):
                if ((self.fir_point.x == x or self.sec_point.x == x) and self.fir_point.y <= y <= self.sec_point.y) or (
                        (self.fir_point.y == y or self.sec_point.y == y) and self.fir_point.x <= x <= self.sec_point.x):
                    field[y][x] = '*'
        return field

    @property
    def square(self):
        return (self.sec_point.x - self.fir_point.x) * (self.sec_point.y - self.fir_point.y)


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.a = p1
        self.b = p2

    def draw(self, field=None):
        if field is None:
            field = [['.' for _ in range(40)] for _ in range(40)]
        vec_x = abs(self.a.x - self.b.x)
        vec_y = abs(self.a.y - self.b.y)
        try:
            delta = max(vec_x, vec_y) / min(vec_x, vec_y)
        except ZeroDivisionError:
            delta = 0
        min_x, max_x = (self.a.x, self.b.x) if self.a.x < self.b.x else (self.b.x, self.a.x)
        min_y, max_y = (self.a.y, self.b.y) if self.a.y < self.b.y else (self.b.y, self.a.y)

        # Текущие координаты точки на прямой
        curr_y = min_y
        curr_x = min_x
        while curr_y <= max_y and curr_x <= max_x:
            field[int(curr_y)][int(curr_x)] = '*'
            if vec_x == 0:
                curr_y += 1
            elif vec_y == 0:
                curr_x += 1
            elif vec_x < vec_y:
                curr_y += delta
                curr_x += 1
            else:
                curr_y += 1
                curr_x += delta
        return field

    @property
    def length(self):
        return ((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2) ** 0.5


class Triangle(Figure):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1)
        self.sec_point = p2
        self.third_point = p3

    # А что вы ещё ждали от псевдографики в консоли на целых числах.........
    def draw(self, field=None):
        if field is None:
            field = [['.' for _ in range(40)] for _ in range(40)]
        l1 = Line(self.fir_point, self.sec_point)
        l2 = Line(self.fir_point, self.third_point)
        l3 = Line(self.sec_point, self.third_point)
        firLine = l1.draw(field)
        secLine = l2.draw(firLine)
        all_lines = l3.draw(secLine)
        return all_lines

    @property
    def square(self):
        a = Line(self.fir_point, self.sec_point).length
        b = Line(self.fir_point, self.third_point).length
        c = Line(self.sec_point, self.third_point).length
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def main():
    p1 = Point(5, 0)
    p2 = Point(8, 3)
    p3 = Point(6, 5)
    arr = [Triangle(p1, p2, p3), Rectangle(p1, p2), Figure(p1)]

    for figure in arr:
        print(figure)

    for figure in arr:
        if isinstance(figure, Line):
            continue
        print(figure.square)


if __name__ == '__main__':
    main()
