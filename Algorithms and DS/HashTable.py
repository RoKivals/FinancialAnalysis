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
        max_len = self.size
        for elem in self.table:
            if elem is not None:
                length = 1
                current = elem
                while current.next:
                    length += 1
                    current = current.next
                max_len = max(max_len, length)
        return max_len

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self._search(key)
            return True
        except KeyError:
            return False


def main():
    pass


# Driver code
if __name__ == '__main__':
    # Create a hash table with
    # a capacity of 5
    ht = HashTable(5)

    # Add some key-value pairs
    # to the hash table
    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)

    # Check if the hash table
    # contains a key
    print("apple" in ht)  # True
    print("durian" in ht)  # False

    # Get the value for a key
    print(ht.search("banana"))  # 2

    # Update the value for a key
    ht.insert("banana", 4)
    print(ht.search("banana"))  # 4

    ht.remove("apple")
    # Check the size of the hash table
    print(len(ht))  # 3
