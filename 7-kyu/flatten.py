# https://www.codewars.com/kata/5250a89b1625e5decd000413/train/python

def flatten(lst):
    res = list()
    for i in lst:
        if type(i) == list:
            res.extend(i)
        else:
            res.append(i)
    return res
