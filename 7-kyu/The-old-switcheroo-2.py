# https://www.codewars.com/kata/55d6a0e4ededb894be000005/train/python

import string

def encode(s):
    a = string.ascii_lowercase
    return ''.join(f'{a.index(i)+1}' if i in a else i for i in s.lower())
