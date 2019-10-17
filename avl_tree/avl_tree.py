"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
      depth_l = depth_r = 0
      if self.node.left is not None:
        #print('node type',type(self.node.left))
        depth_l = 1 + self.node.left.update_height()
      if self.node.right is not None:
        depth_r = 1 + self.node.right.update_height()
      
      self.height = max(depth_l,depth_r)
      return self.height

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
      height_r = height_l = 0
      if self.node.left is not None:
        height_l = self.node.left.update_height()
      if self.node.right is not None:
        height_r = self.node.right.update_height()
      self.balance = (height_r - height_l)
      return self.balance

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        if self.node.right is None:
          pass
        else:
          right_child = self.node.right.node
          self.node.right = None
          old_parent = self.node
          self.node = right_child
          left_save = self.node.left  #added line
          old_parent.right = left_save  #added line to preserve lost data in rotation
          self.node.left = AVLTree(old_parent)

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        if self.node.left is None:
          pass
        else:
          left_child = self.node.left.node
          self.node.left = None
          old_parent = self.node
          self.node = left_child
          right_save = self.node.right
          old_parent.left = right_save
          self.node.right = AVLTree(old_parent)

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        pass
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        pass
