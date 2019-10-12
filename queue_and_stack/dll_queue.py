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
        self.size += 1

    def dequeue(self):
        """`dequeue` should remove and return an item from the front of the queue."""
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        retur self.size
