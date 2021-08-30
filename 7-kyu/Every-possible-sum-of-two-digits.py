# https://www.codewars.com/kata/5b4e474305f04bea11000148/solutions

from itertools import combinations

def digits(n):
    return list(map(sum, combinations(map(int, str(n)), 2)))
