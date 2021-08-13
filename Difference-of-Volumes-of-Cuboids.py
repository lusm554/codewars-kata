# https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python

from functools import reduce

def find_difference(a, b):
    return abs(reduce(lambda x, y: x*y, a)-reduce(lambda x, y: x*y, b))

