# qQueue follows the First in First Out (FIFO) rule - the item that goes in
# first is the item that comes out first. 
# Putting items in the queue is called enqueue, and removing items is called
# dequeue.
# Basic operations: enqueue, dequeue, isEmpty, isFull, peek

class Queue:

    def __init__(self):
        self.queue = []
        self.size = 5
    
    def enqueue(self, item):
        if len(self.queue) > self.size:
            raise IndexError()
        self.queue.append(item) 
        return self
 
    def dequeue(self):
        if len(self.queue) == 0:
            raise ValueError()
        if len(self.queue) < 1: return None
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.size

    def peek(self):
        return self.queue[-1]

