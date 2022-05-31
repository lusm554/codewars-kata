# https://www.codewars.com/kata/5239f06d20eeab9deb00049b/train/python

def fibonacci(n):
    if n <= 0:
        return []
    
    a, b = 0, 1
    r = []
    
    for i in range(n):
        r.append(a)
        a, b = b, b + a
        
    return r

