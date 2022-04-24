# https://www.codewars.com/kata/57a1d5ef7cb1f3db590002af/train/python

def fibonacci(n: int) -> int:
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

