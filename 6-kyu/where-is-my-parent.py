# https://www.codewars.com/kata/58539230879867a8cd00011c/train/python

import itertools
def find_children(dancing_brigade):
    return ''.join(''.join(g).capitalize() for _, g in itertools.groupby(sorted(dancing_brigade.lower())))
