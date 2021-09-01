# https://www.codewars.com/kata/589577f0d1b93ae32a000001/train/python

def sort_by_height(a):
    b = sorted([k for k in a if k != -1])
    return [i if i == -1 else b.pop(0) for i in a]

