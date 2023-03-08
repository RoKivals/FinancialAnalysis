class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


class Workers:
    def __init__(self):
        self.persons = []

    def add_worker(self, name, age):
        tmp = Person(name, age)
        self.persons.append(tmp)

    def display_cnt(self):
        print(len(self.persons))

    def display_workers(self):
        for worker in self.persons:
            print(f"{worker.name} {worker.age}")


class Child(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school


class Childs(Workers):
    def __init__(self):
        super().__init__()

    def add_child(self, name, age, school):
        tmp = Child(name, age, school)
        self.persons.append(tmp)

    def get_school(self):
        for i in self.persons:
            print(f"{i.name} учится в школе №{i.school}")


def main():
    pass


if __name__ == '__main__':
    main()
