# https://www.codewars.com/kata/57ef016a7b45ef647a00002d/train/python

# first solution, more readable
def filter_homogenous(a):
    res = []
    for ar in a:
        if len(ar) == 0: continue
        test = type(ar[0])
        if all(test == type(el) for el in ar):
            res.append(ar)
    return res

# second solution, one line
def filter_homogenous2(a):
    return [ar for ar in a if len(ar) > 0 and all(type(ar[0]) == type(el) for el in ar)]
