import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
       # Insert the given value into the tree
    def insert(self, value):
        #print(self.value)
        if value >= self.value:
          if self.right is None:
            new_node = BinarySearchTree(value)
            self.right = new_node
          else:
            self.right.insert(value)
        elif value < self.value:
          if self.left is None:
            new_node = BinarySearchTree(value)
            self.left = new_node
          else:
            self.left.insert(value)
 


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #print(self.value)
        if self.value == target:
          return True
        elif self.value > target:
          if self.left is None:
            return False
          else:
            return self.left.contains(target)
        elif self.value < target:
          if self.right is None:
            return False
          else:
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
          return self.value
        else:
          return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
          #print(self.value)
          #cb(self.value)
          if self.left is None:
            pass
          else:
            self.left.for_each(cb)
          
          if self.right is None:
            pass
          else:
            self.right.for_each(cb)
            
          cb(self.value)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
      if self.left is not None:
        self.left.in_order_print(self)
        print(self.value)
        if self.right is not None:
          self.right.in_order_print(self.right)
      elif self.left is None:
        print(self.value)
        if self.right is not None:
          self.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
      my_Q = Queue()
      my_Q.enqueue(node)
      while my_Q.storage.head is not None:
        if my_Q.storage.head.value.left is not None:
          my_Q.enqueue(my_Q.storage.head.value.left)
        if my_Q.storage.head.value.right is not None:
          my_Q.enqueue(my_Q.storage.head.value.right)
        print(my_Q.storage.head.value.value)
        my_Q.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
      my_S = Stack()
      my_S.push(node)
      counter = 0
      while my_S.storage.head is not None or counter == 0:
        pushes = []
        if my_S.storage.head.value.left is not None:
          pushes.append(my_S.storage.head.value.left)
        if my_S.storage.head.value.right is not None:
          pushes.append(my_S.storage.head.value.right)
        print(my_S.pop().value)
        for p in pushes:
          my_S.push(p)
        counter += 1

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
