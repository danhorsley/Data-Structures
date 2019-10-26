class Heap:
    def __init__(self, comparator = lambda x,y : x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        my_index = len(self.storage)-1
        self._bubble_up(my_index)
  
        


    def delete(self):
        if len(self.storage)==0:
          return None
        ret = self.storage[0]
        self.storage = self.storage[1:]
        self._sift_down(0)
        return ret

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
          pass
        else:
          while index >0:
            parent_number = (index-1)//2
            if self.comparator(self.storage[index],self.storage[parent_number]):
              a = self.storage[index]
              b = self.storage[parent_number]
              self.storage[index] = b
              self.storage[parent_number] = a
              index = parent_number
            else:
              index = -1
              pass

    def _sift_down(self, index):
        while len(self.storage)>index*2 + 1 and len(self.storage)>1:
          child_number_one = index*2 + 1

          if len(self.storage)>index*2 + 2:
            child_number_two = index*2 + 2
            if self.comparator(self.storage[child_number_one],self.storage[child_number_two]):
              greater_child = child_number_one
            else:
              greater_child = child_number_two
          else:
            greater_child = child_number_one
          #print('i',index, 'g',greater_child)
          if self.comparator(self.storage[greater_child],self.storage[index]):
            a = self.storage[greater_child]
            b = self.storage[index]
            self.storage[index] = a
            self.storage[greater_child] = b
          else:
            index = len(self.storage)
          index = greater_child  