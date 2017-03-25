class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        # Appends item to front of the deque (end of the list)
        self.items.append(item)

    def add_rear(self, item):
        # Inserts item to rear of the deque (beginning of the list)
        self.items.insert(0, item)

    def remove_front(self):
        # Pops item from the front of the deque (end of the list)
        return self.items.pop()

    def remove_rear(self):
        # Pops item from the rear of the deque (beginning of the list)
        return self.items.pop(0)

    def size(self):
        return len(self.items)
