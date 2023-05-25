import unittest


class Position:
    def __init__(self, column: str, row: str):
        self._column = column
        self._row = row

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value: str):
        if 1 <= int(value) <= 8:
            self._row = value
        else:
            raise ValueError("Фигура может попасть только в клетку со строкой от 1 до 8")

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, value: str):
        if 'a' <= value.lower() <= 'h':
            self._column = value
        else:
            raise ValueError("Фигура может попасть только в клетку с столбцом от A до H")

    def __str__(self):
        return self._column.upper() + self._row


class PositionTest(unittest.TestCase):
    def test_map_calculating_road_angle(self):
        test_map = Position('a', '8')
        test_map2 = Position('h', '4')

        test_map3 = Position('m', '9')

        self.assertEqual(test_map.__str__(), 'A8')
        self.assertEqual(test_map3.__str__(), None)


if __name__ == '__main__':
    unittest.main()
