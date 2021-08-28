# https://www.codewars.com/kata/61123a6f2446320021db987d/train/python

from math import trunc

def prev_mult_of_three(n):
    if n == 0: return None
    if n % 3 == 0: return n
    return prev_mult_of_three(trunc(n/10))

