from Positions import *


class Figure:
    def __init__(self, color: str, pos: Position):
        self._color = color
        self._position = pos

    def __str__(self):
        return self._color + str(self._position)

    def is_valid_move(self, move: Position):
        if move == self._position:
            raise ValueError("Вы не можете оставить фигуру на том же месте")

    def change_position(self, new_pos: Position):
        self._position = new_pos


class Pawn(Figure):
    def __init__(self, color: str, pos: Position):
        super().__init__(color, pos)

    def attack_valid(self, goal: Position) -> bool:
        # Белые всегда снизу
        if self._color == 'w':
            if abs(goal.column - self._position.column) == 1 and goal.row - self._position.row == 1:
                return True
        if self._color == 'b':
            if abs(goal.column - self._position.column) == 1 and goal.row - self._position.row == -1:
                return True
        return False

    def is_valid_move(self, move: Position) -> bool:
        if self._color == 'w':
            if move.column == self._position.column and move.row - self._position.row in [1, 2]:
                return True
        if self._color == 'b':
            if move.column == self._position.column and move.row - self._position.row in [-1, -2]:
                return True
        return False


class Knight(Figure):
    def __init__(self, color: str, pos: Position):
        super().__init__(color, pos)

    def is_valid_move(self, move: Position) -> bool:
        if (self._position.row - move.row) ** 2 + (self._position.column - move.column) ** 2 == 5:
            return True
        else:
            return False


class Bishop(Figure):
    def __init__(self, color: str, pos: Position):
        super().__init__(color, pos)

    def is_valid_move(self, move: Position) -> bool:
        if (self._position.column - self._position.row == move.column - move.row) or \
                (self._position.column + self._position.row == move.column + move.row):
            return True
        else:
            return False


class Rook(Figure):
    def __init__(self, color: str, pos: Position):
        super().__init__(color, pos)

    def is_valid_move(self, move: Position) -> bool:
        if self._position.row == move.row or self._position.column == move.column:
            return True
        else:
            return False


class King(Figure):
    def __init__(self, color: str, pos: Position):
        super().__init__(color, pos)

    def is_valid_move(self, move: Position) -> bool:
        if abs(self._position.column - move.column) <= 1 and abs(self._position.column - move.column) <= 1:
            return True
        else:
            return False


class Queen(Figure):
    def __init__(self, color: str, pos: Position):
        super().__init__(color, pos)

    def is_valid_move(self, move: Position) -> bool:
        if abs(self._position.column - move.column) <= 1 and abs(self._position.column - move.column) <= 1 \
                or self._position.row == move.row or self._position.column == move.column:
            return True
        else:
            return False


class FigureMovementTest(unittest.TestCase):
    def test_map_calculating_road_angle(self):
        Pawn1 = Pawn('b', Position('a', '5'))
        Pawn2 = Pawn('w', Position('h', '6'))

        self.assertEqual(Pawn1.is_valid_move(Position('a', '6')), True)


if __name__ == '__main__':
    unittest.main()
