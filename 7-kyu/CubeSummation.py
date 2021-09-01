# https://www.codewars.com/kata/550e9fd127c656709400024d/train/python

def cube_sum(n, m):
    n, m = sorted([n, m])
    return sum(i**3 for i in range(n+1, m+1))

