# https://www.codewars.com/kata/57f6ad55cca6e045d2000627/train/python

from math import sqrt

def square_or_square_root(arr):
    return [sqrt(i) if round(sqrt(i)) == sqrt(i) else i**2 for i in arr]  

