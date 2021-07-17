# What difference between priority queue and normal queue?
# In a noraml queue, the first-in-first-out rule is implemented whereas, in a
# priority queue, the values are removed on the basis of priority. The item with
# the highest pripority is removed first.
# Basic operations of a pripority queue are inserting, removing, and peeking
# items.

class MaxHeap:
    def __init__(self, tree=[]):
        self.tree = tree

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.tree[i] < self.tree[l]:
            largest = l
        if r < n and self.tree[largest] < self.tree[r]:
            largest = r
        if largest != i:
            self.tree[i], self.tree[largest] = self.tree[largest], self.tree[i]

    def insert(self, new):
        size = len(self.tree)
        if size == 0:
            self.tree.append(new)
        else:
            self.tree.append(new)
            for i in range((size//2)-1, -1, -1):
                self.heapify(size, i)

    def deleteNode(self, num):
        size = len(self.tree)
        i = 0
        for i in range(size):
            if num == self.tree[i]:
                break
        self.tree[i], self.tree[size-1] = self.tree[size-1], self.tree[i]
        self.tree.remove(num)
        for i in range((len(self.tree)//2)-1, -1, -1):
            self.heapify(len(self.tree), i)

# Priority by max value in queue
class PriorityQueue:
    def __init__(self):
        self.tree = []
        self.heap = MaxHeap(self.tree)

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        temp = self.tree[-1]
        self.heap.deleteNode(temp)
        return temp

    def size(self):
        return len(self.tree)

    def peek(self):
        return self.tree[-1]

# TEST
q = PriorityQueue()

q.enqueue(1)
print(q.size())
q.enqueue(2)
print(q.peek())
print(q.dequeue())
print(q.size())

