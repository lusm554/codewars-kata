# Circular queue is the extended version of a regular queue where the last item
# is connected to the first item. Thus forming a cricle-like strucuture.

class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if (self.tail + 1) % self.k == self.head:
            raise IndexError('queue is full')
        
        if self.head == -1:
            self.head = self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data



q = CircularQueue(5)

q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
