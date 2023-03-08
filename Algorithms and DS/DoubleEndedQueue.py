class Node:
    def __init__(self, value, prevn, nextn):
        self.value = value
        self.prev_node = prevn
        self.next_node = nextn


class DoubleEndedQueue:
    def __init__(self, first=None, last=None):
        self.head = first
        self.tail = last

    # Insert in the begin of Queue
    def push_front(self, value):
        if self.head is None:
            tmp = Node(value, None, None)
            self.head = tmp
            self.tail = tmp
        else:
            tmp = Node(value, None, self.head)
            self.head.prev_node = tmp
            self.head = tmp

    # Insert in the end of Queue
    def push_back(self, value):
        if self.tail is None:
            tmp = Node(value, None, None)
            self.head = tmp
            self.tail = tmp
        else:
            tmp = Node(value, self.tail, None)
            self.tail.next_node = tmp
            self.tail = tmp

    # Delete elem from the begin of Queue  
    def pop_front(self):
        if self.head is None:
            return None
        res = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
        return res

    # Delete elem from the end of Queue      
    def pop_back(self):
        if self.tail is None:
            return None
        res = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
        return res

    def is_empty(self) -> bool:
        return self.head is None

    def clear(self):
        while self.head is not None and self.tail is not None:
            self.pop_back()
            self.pop_front()

    def direct_iter(self):
        curr = self.head
        while curr is not None:
            yield curr.value
            curr = curr.next_node

    def reverse_iter(self):
        curr = self.tail
        while curr is not None:
            yield curr.value
            curr = curr.prev_node

    def __len__(self):
        res = 0
        for _ in self.direct_iter():
            res += 1
        return res