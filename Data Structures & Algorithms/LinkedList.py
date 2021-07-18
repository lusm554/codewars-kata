from random import randint

# A linked list is a linear ds that includes a series of connected nodes. Each
# node store the data and the address of the next node.
# Basic linked list operations:
# Traversal - access each item of the linked list
# Insertion - adds item to the linked list
# Deletion - removes item from list
# Search - find a node in the linked list
# Sort - sort the nodes of the linked list

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sort(self):
        _n = self.head
        while _n:
            n = self.head
            _next = n.next
            prev = None
            while _next:
                if n.item > _next.item:
                    if not prev:
                        prev = n.next
                        _next = _next.next
                        prev.next = n
                        n.next = _next
                        self.head = prev
                    else:
                        temp = _next
                        _next = _next.next
                        prev.next = n.next
                        prev = temp
                        temp.next = n
                        n.next = _next
                else:
                    prev = n
                    n = _next
                    _next = _next.next
            _n = _n.next
           

    def search(self, item):
        n = self.head 
        while n:
            if n.item == item:
                return n
            n = n.next
        return False

    def delete(self, index):
        n, i = self.head, 0
        if index == 0:
            self.head = n.next
            return
        while n:
            if i == index-1:
                _next = n.next.next
                n.next = _next
                break
            i += 1
            n = n.next

    def insert(self, item):
        n = self.head
        while n:
            if not n.next:
                n.next = Node(item)
                return
            n = n.next

    def insertAfter(self, prev, item):
        new = Node(item)
        new.next, prev.next = prev.next, new

    def insertFirst(self, item):
        new = Node(item)
        new.next, self.head = self.head, new

    def traversal(self):
        items = []
        n = self.head
        while n:
            items.append(n.item)
            n = n.next
        print(items) # REMOVE
        return items

if __name__ == '__main__':
    # TEST
    l = LinkedList()
    l.head = Node(0)
    nodes = [l.head]
    test = Node('test')
    for i in range(1, 10):
        nodes.append(Node(randint(1, 100)))
    for i in range(len(nodes)-1):
        f, s = nodes[i], nodes[i+1]
        f.next = s
    l.traversal()
    l.sort()
    l.traversal()
