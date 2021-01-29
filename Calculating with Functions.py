# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
# callable(arg) - checks and returns True if the object passed appears to be callable, otherwise False.

def zero(a=None): return a(0) if callable(a) else 0
def one(a=None): return a(1) if callable(a) else 1
def two(a=None): return a(2) if callable(a) else 2
def three(a=None): return a(3) if callable(a) else 3
def four(a=None): return a(4) if callable(a) else 4
def five(a=None): return a(5) if callable(a) else 5
def six(a=None): return a(6) if callable(a) else 6
def seven(a=None): return a(7) if callable(a) else 7
def eight(a=None): return a(8) if callable(a) else 8
def nine(a=None): return a(9) if callable(a) else 9
    
def plus(a): return lambda num: num + a
def minus(a): return lambda num: num - a
def times(a): return lambda num: num * a
def divided_by(a): return lambda num: num // a

print(seven(times(five()))) # 35
print(four(plus(nine()))) # 13
print(eight(minus(three()))) # 5
print(six(divided_by(two()))) # 3
