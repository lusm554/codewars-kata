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


s = Stack()
s.push(1)
print(s.pop()) # 1
print(s.is_full()) # False
print(s.length()) # 0

for i in range(10):
    s.push(i)

print(s.length()) # 10
try: 
    s.push(1)
except OverflowError:
    print('OverflowError')

s = Stack()
try:
    s.pop()
except IndexError:
    print('IndexError')
