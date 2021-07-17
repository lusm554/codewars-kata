# Circular queue is the extended version of a regular queue where the last item
# is connected to the first item. Thus forming a cricle-like strucuture.

class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # add item to queue
    def enqueue(self, data):
        if (self.tail + 1) % self.k == self.head:
            raise IndexError('queue is full')
        
        if self.head == -1:
            self.head = self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # remove item from queue
    def dequeue(self):
        if self.head == -1:
            raise IndexError('queue is empty')
        
        if self.head == self.tail:
            temp = self.queue[self.head]
            self.head = self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

q = CircularQueue(5) 
for i in range(5):
    q.enqueue(i)

try:
    q.enqueue('ggwp')
except IndexError:
    print('it\'s ok')

for i in range(5):
    e = q.dequeue()
    print(e)

try:
    q.dequeue()
except IndexError:
    print('all done')
