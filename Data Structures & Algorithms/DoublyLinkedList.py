# In doubly linked list each node has pointer to the previous node. Thus, we can
# go either direction: forward of backward.

class Node:
    def __init__(self, item):
        self.item = item
        self.next = self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    

if __name__ == '__main__':
    # TEST
    l = DoublyLinkedList()
    l.head = Node('start')
    # Create nodes
    nodes = [Node(i) for i in range(10)]
    nodes.insert(0, l.head)
    # Merge nodes
    for i in range(len(nodes)-1):
        c, n = nodes[i], nodes[i+1]
        c.next = n 
        if (i-1) >= 0:
            c.prev = nodes[i-1]
        if i == (len(nodes)-2):
            n.prev = c
    # from beginning
    n = l.head
    while n:
        print(n.item)
        n = n.next
    # from the end
    n = nodes[-1]
    while n:
        print(n.item)
        n = n.prev
