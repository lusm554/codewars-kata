class Stack:


    def __init__(self):
        self.MAX_LEN = 10
        self.data = []


    def length(self):
        return len(self.data)


    def is_full(self):
        if len(self.data) == self.MAX_LEN:
            return True
        return False


    def push(self, item):
        if len(self.data) < self.MAX_LEN:
            self.data.append(item)
        else:
            raise OverflowError()


    def pop(self):
        if len(self.data) == 0:
            raise IndexError('Stack is empty.') 
        else:
            return self.data.pop()
