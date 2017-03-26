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
        current = self.head
        while current:
            if current.get_data == item:
                return True
            else:
                if current.get_data > item:
                    return False
                elif current.get_next is None:
                    return False
                else:
                    current = current.get_next

    def add(self, item):
        # Could maybe be simpler.
        temp = Node(item)
        current = self.head
        previous = None
        while current:
            if current.get_data > item:
                break
            else:
                previous = current
                current = current.get_next
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
        while current:
            count += 1
            current = current.get_next

        return count

    def __iter__(self):
        """For debugging purposes, anytime iteration is called it yields all of the node objects."""
        current = self.head
        while current:
            yield current.get_data
            current = current.get_next