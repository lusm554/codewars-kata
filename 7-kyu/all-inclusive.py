# https://www.codewars.com/kata/5700c9acc1555755be00027e/train/python

def contain_all_rots(s, arr):
    arr = set(arr)
    if all((s[i:]+s[:i]) in arr for i in range(len(s))):
        return True
    return False
