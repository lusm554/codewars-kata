# https://www.codewars.com/kata/62a611067274990047f431a8/train/python

def alternate(n, f, s):
    return [f if i % 2 == 0 else s for i in range(n)] 

