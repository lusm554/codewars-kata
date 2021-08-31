# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python

def solve(s):
    u, l = sum(map(str.isupper, s)), sum(map(str.islower, s))
    return s.upper() if u > l else s.lower()
