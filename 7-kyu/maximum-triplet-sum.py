# https://www.codewars.com/kata/5aa1bcda373c2eb596000112/train/python

import itertools
def max_tri_sum(numbers):
    return max(sum(c) for c in itertools.combinations(set(numbers), 3))
