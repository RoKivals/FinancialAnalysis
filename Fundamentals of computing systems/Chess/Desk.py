class Desk:
    def __init__(self, white: list, black: list):
        self.field = set(white + black)

    def check_correct_fields(self):
        pass

    def figure_in_cell(self, cell: str):
        return self.field[cell] is None

    def color_of_figure(self, cell):
        return self.field[cell].color
