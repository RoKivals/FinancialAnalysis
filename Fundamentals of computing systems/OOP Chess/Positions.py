import unittest


class Position:
    def __init__(self, column: str, row: str):
        if 'a' <= column.lower() <= 'h':
            self._column = column
        else:
            raise ValueError("Фигура может находиться только в столбце от A до H")

        if 1 <= int(row) <= 8:
            self._row = row
        else:
            raise ValueError("Фигура может находиться только в строке от 1 до 8")

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
        test_pos = Position('a', '8')
        test_pos2 = Position('h', '4')
        test_pos4 = Position('A', '1')

        self.assertEqual(test_pos.__str__(), 'A8')
        self.assertEqual(test_pos2.__str__(), 'H4')
        self.assertEqual(test_pos4.__str__(), 'A1')

        try:
            test_pos3 = Position('M', '9')
        except ValueError:
            print('Выход за пределы поля')


if __name__ == '__main__':
    unittest.main()
