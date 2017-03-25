class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        # Add item to the end of the queue (front of the list).
        self.items.insert(0, item)

    def dequeue(self):
        # Remove item from the front of the queue (end of the list).
        return self.items.pop()

    def size(self):
        return len(self.items)
