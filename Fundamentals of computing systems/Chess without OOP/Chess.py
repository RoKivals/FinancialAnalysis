class Figure:
    pass


def create_field():
    letters = 'ABCDEFGH'
    digits = [i for i in range(1, 9)]
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
