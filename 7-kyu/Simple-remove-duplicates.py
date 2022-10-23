# https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/python

def solve(arr): 
    r = []
    for x in arr[::-1]:
        if x not in r:
            r.append(x)
    return r[::-1]

