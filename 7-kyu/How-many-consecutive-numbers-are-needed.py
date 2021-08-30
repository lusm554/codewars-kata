# https://www.codewars.com/kata/559cc2d2b802a5c94700000c/train/python

# simple solution
def consecutive(arr):
    if not len(arr): return 0
    res = 0
    for i in range(min(arr), max(arr)+1):
        if i not in arr:
            res += 1
    return res
    
def consecutive2(arr):
    return 0 if not len(arr) else sum(1 for i in range(min(arr), max(arr)+1) if i not in arr)
