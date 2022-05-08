# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(a):
    res = set(j for r in a for j in range(*r))
    return len(res)

