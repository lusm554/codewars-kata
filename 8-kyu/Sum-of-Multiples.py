# https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python

def sum_mul(n, m):
    return "INVALID" if m <= 0 or n <= 0 else sum(range(n, m, n))

