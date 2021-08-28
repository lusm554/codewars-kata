# https://www.codewars.com/kata/5b6b128783d648c4c4000129/train/python

from functools import reduce

def smallest_product(a):
    return min(reduce(lambda prev, curr: prev * curr, l) for l in a)

