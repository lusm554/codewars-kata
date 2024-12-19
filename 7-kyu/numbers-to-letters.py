# https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c/train/python

import string
def switcher(arr):
  s = '_' + string.ascii_lowercase[::-1] + '!? '
  return ''.join(s[int(x)] for x in arr)
