# Heap ds is a complete binary tree that satisfies the heap property where any
# given node is:
# - always greater than its child nodes and the key of the root node i the
# largest among all other nodes. This property is also called max heap property.
# - always smaller than the child node and the key of the root node is the
# smallest among all other nodes. This property is also called min heap
# property.
#         max heal property
#               9
#              / \
#             /   \
#            5     4
#           / \   / 
#          /   \ /     
#         1    3 4


class MaxHeap:
    def __init__(self, tree):
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

# TEST
k = [3, 9, 2, 1, 4, 5]
l = []

j = MaxHeap(l)
for i in k:
    j.insert(i)

print(j.tree)

j.deleteNode(3)
print(j.tree)

