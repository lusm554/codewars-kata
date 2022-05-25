# https://www.codewars.com/kata/57a6633153ba33189e000074/train/python

from collections import Counter

def ordered_count(inp):
    return list(Counter(inp).items())

