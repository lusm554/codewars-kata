# In Circular Linked List last item is linked to the first item. This forms a
# circular loop. 
# A circular linked list can be either singly linked or doubly linked.
# - for singly linked list, next pointer of last item poitns to the first item.
# - in the doubly linked list, prev pointer of the first item points to the last
# item as well.

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        n = self.head
        while n:
            if not n.next:
                new = Node(item) 
                #new.next = self.head
                n.next = new 
                return
            n = n.next


if __name__ == '__main__':
    # TEST
    l = CircularLinkedList()
    l.head = Node('start')
    for i in range(10):
        l.insert(i)
    n = l.head
    while n:
        print(n.item)
        n = n.next
