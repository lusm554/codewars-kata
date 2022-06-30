# https://www.codewars.com/kata/59126cd3379de6ca5f00019c/train/python

def case_unification(s):
    upp = [ch.isupper() for ch in s].count(True)
    return s.upper() if upp > (len(s)-upp) else s.lower()

