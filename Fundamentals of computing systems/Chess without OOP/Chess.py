letters = 'ABCDEFGH'
digits = [i for i in range(1, 9)]


def fill_field_by_default(field: set):
    for col in letters:
        field[f'{col}2'] = 'Pawn'
        field[f'{col}7'] = 'Pawn'
    

def create_field():
    field = set()
    for col in letters:
        for row in digits:
            field.add(f'{col}{row}')
    return field


def check_cell(cell: str, field: set):
    cell = cell.capitalize()
    return cell in field


def main():
    pass


if __name__ == '__main__':
    main()
