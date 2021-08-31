# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python

def solve(arr):
    a = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    for i in arr:
        r = sum([1 for j, k in zip(a, i.lower()) if j == k])
        res.append(r)
    return res
