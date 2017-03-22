class Stack:
    """Implements a basic stack using python lists."""
    
    def __init__(self):
        """Creates an empty list on initialization."""
        self.items = []

    def is_empty(self):
        """Returns a bool stating if stack is empty or not."""
        return self.items == []

    def push(self, item):
        """Pushes item to stack, placing it on top."""
        self.items.append(item)

    def pop(self):
        """Pops last item off of the stack."""
        return self.items.pop()

    def peek(self):
        """Returns item currently on the top of the stack without popping."""
        return self.items[len(self.items)-1]

    def size(self):
        """Returns the count of items in the stack."""
        return len(self.items)

class ReverseStack:
    """Implements a stack where the top is at the beginning."""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
