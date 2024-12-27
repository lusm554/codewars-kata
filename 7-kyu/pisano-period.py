# https://www.codewars.com/kata/5f1360c4bc96870019803ae2/train/python

def pisano(n):
    a, b = 0, 1
    for i in range(n*n):
        a, b = b, (a + b) % n
        if a == 0 and b == 1:
            return i + 1
