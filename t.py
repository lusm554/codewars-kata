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
size = len(a)
alloc = [(0, 4)]
f = list(islice(a, *alloc[0]))
print(f)

i=0
free_s = 0
while i < size:
  print(f"{i=}")
  if any(i >= x[0] and i <= x[1] for x in alloc):
    print('\t', free_s)
    free_s = 0
  else:
    free_s += 1
  i+=1

print('\t', free_s)






