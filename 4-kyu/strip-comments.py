# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

import re
def strip_comments(s, markers):
    if len(markers) == 0: return s
    s = s.split('\n')
    s = [re.split('|'.join(map(re.escape, markers)), s)[0].rstrip() for s in s]
    return '\n'.join(s)
