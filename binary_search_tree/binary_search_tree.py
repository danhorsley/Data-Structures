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
            new_node.left = self
            self.right = new_node
          elif value <= self.right.value:
            new_node = BinarySearchTree(value)
            new_node.left = self
            new_node.right = self.right
            self.right.left = new_node
            self.right = new_node
          else:
            self.right.insert(value)
        elif value < self.value:
          if self.left is None:
            new_node = BinarySearchTree(value)
            new_node.right = self
            self.left = new_node
          elif value >= self.left.value:
            new_node = BinarySearchTree(value)
            new_node.left = self.left
            new_node.right = self
            self.left.right = new_node
            self.left = new_node
          else:
            self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #print(self.value)
        if self.value == target:
          return True
        elif self.value < target:
          if self.right is None or self.right.value>target:
            return False
          else:
            return self.right.contains(target)
        elif self.value > target or self.left.value<target:
          if self.left is None:
            return False
          else:
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
          return self.value
        else:
          return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb, direction='r'):
          #print(self.value)

          if direction =='r':
            if self.right is None:

              self.left.for_each(cb,direction = 'l')
              return cb(self.value)
            else:
              self.right.for_each(cb)
          elif direction =='l':
            if self.left is None:
              return cb(self.value)
            else:
              self.left.for_each(cb, direction ='l')
              return cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
