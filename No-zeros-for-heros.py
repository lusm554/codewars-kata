# https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python

def no_boring_zeros(n):
    return int(str(n).rstrip('0') or n)
