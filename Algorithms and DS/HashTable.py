import string
import random
from typing import List, Tuple, Union


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.size = 0
        self.table: List[Union[None, Node]] = [None] * capacity

    # Метод деления
    def _hash_key(self, key):
        res = 0
        if isinstance(key, (int, float)):
            res = int(key % self.capacity)
        elif isinstance(key, str):
            summa = 0
            for cnt, sym in enumerate(key):
                summa += ord(sym) * cnt
                res = summa % self.capacity
        elif isinstance(key, (List[str, int, float], Tuple[str, int, float])):
            summa = 0
            for elem in key:
                summa += hash(elem)
                res = summa % self.capacity
        else:
            try:
                hash(key) % self.capacity
            except TypeError:
                raise TypeError("Этот объект нельзя хэшировать")
        return res

    def insert(self, key, value):
        index = self._hash_key(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def _search(self, key):
        index = self._hash_key(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key, "такого ключа нет")

    def remove(self, key):
        index = self._hash_key(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def longest_chain(self):
        max_len = 0
        for elem in self.table:
            if elem is not None:
                length = 1
                current = elem
                while current.next:
                    length += 1
                    current = current.next
                max_len = max(max_len, length)
        return max_len

    def shortest_chain(self):
        min_len = self.size
        for elem in self.table:
            if elem is not None:
                length = 1
                current = elem
                while current.next:
                    length += 1
                    current = current.next
                min_len = min(min_len, length)
        return min_len

    def fill_factor(self):
        empty = 0
        for elem in self.table:
            if elem is None:
                empty += 1
        return (self.size - empty) / self.size

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self._search(key)
            return True
        except KeyError:
            return False


def generate_random_string(length: int):
    letters = string.ascii_letters
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def main():
    table = HashTable()
    # Генерация строк
    for i in range(500):
        key = random.randrange(50000)
        val = generate_random_string(key % 25)
        table.insert(key, val)

    # Генерация чисел
    for i in range(500):
        key = random.randrange(50000)
        val = random.randrange(50000)
        table.insert(key, val)

    print(table.shortest_chain())
    print(table.longest_chain())
    print(table.fill_factor())


if __name__ == '__main__':
    main()
