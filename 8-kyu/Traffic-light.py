# https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python

class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

class TrafficLinkedList:
    def __init__(self):
        green = Node('green')
        yellow = green.next = Node('yellow')
        red = yellow.next = Node('red')
        red.next = green
        self.head = green

    def findNext(self, v):
        h = self.head
        while h.next:
            if h.value == v:
                return h.next
            h = h.next


def update_light(c):
    return TrafficLinkedList().findNext(c).value

