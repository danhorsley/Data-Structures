import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        """`enqueue` should add an item to the back of the queue."""
        self.storage.add_to_tail(value)
        self.size =self.storage.length

    def dequeue(self):
        """`dequeue` should remove and return an item from the front of the queue."""
        ret = self.storage.remove_from_head()
        self.size = self.storage.length
        return ret

    def len(self):
        return self.size
