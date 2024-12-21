# https://www.codewars.com/kata/56582133c932d8239900002e/train/python

import collections
def most_frequent_item_count(c):
    if len(c) == 0: return 0
    return collections.Counter(c).most_common(1)[0][1]
