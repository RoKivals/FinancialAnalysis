from Positions import *


class Figure:
    def __init__(self, color: str, pos: Position):
        self._color = color
        self._position = pos

    def __str__(self):
        return self._color + str(self._position)

    def is_valid_move(self):
        pass

    def change_position(self, new_pos: Position):
        self._position = new_pos


class Pawn(Figure):
    def __init__(self, color: str, pos: Position):
        super().__init__(color, pos)

    def is_valid_move(self):
        pass