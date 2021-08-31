# https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python

def largest_pair_sum(n):
    return sum(sorted(n, reverse=True)[:2])
