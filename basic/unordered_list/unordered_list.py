class Node:
    """
    The node is the building block for a linked list, 
    it must contain the data of the node and a reference to the next node.
    A reference to None will denote the fact that there is no next node. 
    """
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    @property
    def get_data(self):
        return self.data

    @property
    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    """
    This will be our list, initially it has no items.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    @property
    def is_empty(self):
        return self.head is None

    def add(self, item):
        """
        Pretty simple, we add an item by creating a new node and setting it's link to the head of 
        our list, then setting the head of our list to the new item. 
        If it's the first item it becomes the tail.
        """
        temp = Node(item)
        temp.set_next(self.head)
        if self.tail is None:
            self.tail = temp

        self.head = temp

    @property
    def size(self):
        """Returns length of the list."""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next

        return count

    def search(self, item):
        """Finds item, returns boolean."""
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data == item:
                found = True
            else:
                current = current.get_next

        return found

    def remove(self, item):
        """Removes the item from the list, and fixes links."""
        # Could maybe be simpler
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data == item:
                found = True
            else:
                previous = current
                current = current.get_next
        if previous is None:
            self.head = current.get_next
        elif current == self.tail:
            self.tail = previous
            previous.set_next(current.get_next)
        else:
            previous.set_next(current.get_next)

    def append(self, item):
        """
        Adds a new item to the end of the list making it the last item in the collection. I forgot 
        while making this O(1) that I would need to ensure that self.tail always stayed connected 
        when other methods added or removed items.
        """
        current = self.tail
        temp = Node(item)
        current.set_next(temp)
        self.tail = temp

    def index(self, item):
        """Returns the position of item in the list. It needs the item and returns the index."""
        # This could maybe be simpler.
        current = self.head
        found = False
        index = 0
        while current and not found:
            if current.get_data == item:
                found = True
            else:
                current = current.get_next
                index += 1

        return index

    def insert(self, pos, item):
        """Adds a new item to the list at position pos. It needs the item and returns nothing."""
        # This could probably be simpler
        temp = Node(item)
        current = self.head
        index = 0
        previous = None
        while pos > index:
            previous = current
            current = current.get_next
            index += 1
        if previous is None:
            temp.set_next(current)
            self.head = temp
        elif current == self.tail:
            self.tail = temp
            previous.set_next(temp)
        else:
            previous.set_next(temp)
            temp.set_next(current)

    def pop(self):
        """Removes and returns the last item in the list. It needs nothing and returns the item."""
        # Maybe could be simpler
        current = self.head
        previous = None
        while current is not self.tail:
            previous = current
            current = current.get_next
        if previous is None:
            self.head = current.get_next
        elif current == self.tail:
            self.tail = previous
            previous.set_next(current.get_next)
        else:
            previous.set_next(current.get_next)

    def __iter__(self):
        """For debugging purposes, anytime iteration is called it yields all of the node objects."""
        current = self.head
        while current:
            yield current.get_data
            current = current.get_next
