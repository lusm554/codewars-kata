# Deque or Double Ended Queue is a type of queue in which insertion and
# removal of items can either be performed from the front or the rear. Thus, it
# does not follow FIFO rule(First In First Out).
# Types of Deque:
# - Input restricted deque - input is restricted at a single end but allows
# deletion at both the ends.
# - Output restricted deque - output is restricted at a single end but allows
# insertion at both the ends.

class Deque:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def addRear(self, item):
        self.queue.append(item)

    def addFront(self, item):
        self.queue.insert(0, item)

    def rmFront(self):
        if len(self.queue) == 0: raise IndexError()
        return self.queue.pop(0)
    
    def rmRear(self):
        if len(self.queue) == 0: raise IndexError()
        return self.queue.pop()

    def size(self):
        return len(self.queue)

# TEST
q = Deque()
print(q.isEmpty())
q.addRear(1)
q.addFront(2)
print(q.size())
q.rmFront()
q.rmRear()
print(q.size())
try:
    q.rmFront()
except IndexError:
    print('good')
