# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

import string
def printer_error(s):
  colors = string.ascii_lowercase[:string.ascii_lowercase.index('m')+1] 
  error_rate = 0
  for c in s:
    if c in colors: continue
    error_rate += 1
  return f"{error_rate}/{len(s)}"
