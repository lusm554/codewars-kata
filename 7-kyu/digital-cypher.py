# https://www.codewars.com/kata/592e830e043b99888600002d/train/python

import string
import itertools
def encode(msg, key):
    alp = '_'+string.ascii_lowercase  
    encoded = list() 
    key = itertools.cycle(str(key))
    for c in msg:
        encoded.append(alp.index(c) + int(next(key)))
    return encoded
