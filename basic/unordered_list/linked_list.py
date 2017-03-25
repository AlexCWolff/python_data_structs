class Node:
    """
    The node is the building block for the linked list, 
    it must contain the data of the node and a reference to the next node.
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
