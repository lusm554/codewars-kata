# https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python

import re
import string as _s

def solve(s):
    s = re.split('a|e|i|o|u', s)
    return max(sum(map(lambda x: _s.ascii_lowercase.index(x)+1, i)) for i in s)

