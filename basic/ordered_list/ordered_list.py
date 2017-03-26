class Node:
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


class OrderedList:
    """
    This class is like the unordered list, except that entries are added in ascending order. 
    I could put in all the extra methods I added for the unordered list, but you get the point.
    """
    def __init__(self):
        self.head = None

    def search(self, item):
        """
        Since the list is ordered we know that if the number we are looking for is 
        between two entries, it does not exist and we can exit early.
        """
        # This can definitely be simpler.
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data == item:
                found = True
            else:
                if current.get_data > item:
                    stop = True
                else:
                    current = current.get_next

        return found

    def add(self, item):
        # Could maybe be simpler.
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data > item:
                stop = True
            else:
                previous = current
                current = current.get_next

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    @property
    def is_empty(self):
        return self.head is None

    @property
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next

        return count
