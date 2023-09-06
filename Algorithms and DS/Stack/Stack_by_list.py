class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception('Stack is empty')

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception('Stack is empty')

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)