# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python

class Add(int):
    def __call__(self, n):
        return Add(self + n)
    
def add(n):
    return Add(n)

