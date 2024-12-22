# https://www.codewars.com/kata/526dbd6c8c0eb53254000110/train/python

import string
def alphanumeric(pwd):
    if pwd == '': return False
    valid_char_set = string.digits + string.ascii_letters
    return all(c in valid_char_set for c in pwd)
