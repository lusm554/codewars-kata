# https://www.codewars.com/kata/5893fa478a8a23ef82000031/train/python

def palindrome_rearranging(s):
    return sum(s.count(c) % 2 for c in set(s)) < 2

