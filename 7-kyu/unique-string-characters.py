# https://www.codewars.com/kata/5a262cfb8f27f217f700000b/train/python

def solve(a,b):
    inter = set(a) & set(b)
    return ''.join(x for x in a if x not in inter) + ''.join(x for x in b if x not in inter)
