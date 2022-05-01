# https://www.codewars.com/kata/59be6bdc4f98a8a9c700007d/train/python

def remove_chars(s):
    return ''.join(c for c in s if c.isalpha() or c == ' ')

