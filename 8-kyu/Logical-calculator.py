# https://www.codewars.com/kata/57096af70dad013aa200007b/train/python

from functools import reduce

def logical_calc(l, op):
    ops = {
        'AND': lambda a, b: a and b,
        'OR': lambda a, b: a or b,
        'XOR': lambda a, b: not b if a else b
    }
    return reduce(ops[op], l)

