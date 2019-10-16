class Heap:
    def __init__(self, comparator = lambda x,y : x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        #for i in range(len(self.storage)):
        for i in range(1,len(self.storage)):
          #self._bubble_up(i)
          self._sift_down(i)
          self._bubble_up(len(self.storage)-i)


    def delete(self):
        if len(self.storage)==0:
          return None
        ret = self.storage[0]
        self.storage = self.storage[1:]
        return ret

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
          pass
        else:
          parent_number = (index-1)//2
          if self.comparator(self.storage[index],self.storage[parent_number]):
            a = self.storage[index]
            b = self.storage[parent_number]
            self.storage[index] = b
            self.storage[parent_number] = a
          else:
            pass

    def _sift_down(self, index):
        if len(self.storage)>index*2 + 1:
          child_number_one = index*2 + 1

          if len(self.storage)>index*2 + 2:
            child_number_two = index*2 + 2
            if self.comparator(self.storage[child_number_one],self.storage[child_number_two]):
              greater_child = child_number_one
            else:
              greater_child = child_number_two
          else:
            greater_child = child_number_one
          if self.comparator(self.storage[greater_child],self.storage[index]):
            a = self.storage[greater_child]
            b = self.storage[index]
            self.storage[index] = a
            self.storage[greater_child] = b
        else:
          pass