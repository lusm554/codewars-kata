# https://www.codewars.com/kata/5acbc3b3481ebb23a400007d/train/python

def is_flush(cards):
    return len(set(s[-1] for s in cards)) == 1

