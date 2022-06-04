# https://www.codewars.com/kata/59da47fa27ee00a8b90000b4/train/python

from itertools import combinations

def solve(s):
    vals = [int(s[x:y]) for x, y in combinations(range(len(s) + 1), r=2)]
    return len([v for v in vals if v%2!=0])
    
