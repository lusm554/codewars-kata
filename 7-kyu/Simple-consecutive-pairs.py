# https://www.codewars.com/kata/5a3e1319b6486ac96f000049/train/python

def pairs(ar):
    return sum(1 for j in [[ar[i-1], ar[i]] for i in range(1, len(ar), 2)] if j[1] - j[0] in (1, -1))
