# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python

from string import ascii_letters, digits

def solve(s):
    u, l = sum(map(str.isupper, s)), sum(map(str.islower, s))
    n, s, = sum(1 for i in s if i.isdigit()), sum(1 for i in s if set(i).difference(ascii_letters + digits))
    return [u, l, n, s]
