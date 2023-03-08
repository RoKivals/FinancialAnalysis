class Employee:
    pass


class Teacher:
    def __init__(self, disciplines=None):
        if disciplines is None:
            disciplines = []
        self.disciplines = disciplines

    def __str__(self):
        res = "Данный учитель преподаёт следующие предметы: "
        res += ' '.join('\n' + i if (num != 0 and num % 6 == 0) else i for num, i in enumerate(self.disciplines))
        return res

    def add_discipline(self, new_discipline):
        self.disciplines.append(new_discipline)

    def del_discipline(self, name_discipline):
        self.disciplines.remove(name_discipline)


def main():
    t = Teacher(['Math', 'Rus', 'Eng'])
    print(t)
    t.add_discipline('VBA')
    t.del_discipline('Math')
    print(t)


if __name__ == '__main__':
    main()
