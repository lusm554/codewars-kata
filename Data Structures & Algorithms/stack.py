# Stack is a linear ds that follows the principle of Last in First Out (LIFO).
# Basic operations of stack: push, pop, isEmpty, isFull, peek

class Stack:
    def __init__(self):
       self.stack = [] 
       self.TOP = -1
       self.MAX_DEPTH = 99 # like 100, but 99

    def push(self, val):
        if self.TOP >= self.MAX_DEPTH:
            raise IndexError('Stack is full')
        self.stack.append(val)
        self.TOP += 1
        return self

    def pop(self):
        if self.TOP == -1:
            raise ValueError('Stack empty')
        self.TOP -= 1
        return self.stack.pop()

    def isEmpty(self):
        return self.TOP == -1

    def isFull(self):
        return self.TOP == self.MAX_DEPTH 

    def peek(self):
        return self.stack[self.TOP]

