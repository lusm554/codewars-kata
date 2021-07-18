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


if __name__ == '__main__':
    # TEST
    l = LinkedList()
    l.head = Node(0)
    nodes = [l.head]
    for i in range(1, 10):
        nodes.append(Node(i))
    for i in range(len(nodes)-1):
        f, s = nodes[i], nodes[i+1]
        f.next = s
    l = l.head
    while l:
        print(l.item)
        l = l.next
