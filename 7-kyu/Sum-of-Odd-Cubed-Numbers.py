# https://www.codewars.com/kata/580dda86c40fa6c45f00028a/train/python

def cube_odd(arr):
    if any(map(lambda x: not type(x) == int, arr)):
        return None
    return sum(j**3 for j in arr if j**3 % 2 != 0)

