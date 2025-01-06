from itertools import islice
class MemoryManager:
  def __init__(self, memory):
    self.memory = memory
    self.alloc = []

  def allocate(self, size):
    # check free blocks
    # mark block allocated
    # return pointer
    pass

  def release(self, pointer):
    # check pointer in allocated block 
    # mark block as free
    # merge neighbour free blocks 
    pass

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
alloc = [(0, 4)]
f = list(islice(a, *alloc[0]))
print(f)



