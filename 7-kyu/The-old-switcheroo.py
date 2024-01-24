# https://www.codewars.com/kata/55d410c492e6ed767000004f/train/python

def vowel_2_index(s):
    return ''.join(str(n) if ch.lower() in 'aeiou' else ch for n, ch in enumerate(s, start=1))
