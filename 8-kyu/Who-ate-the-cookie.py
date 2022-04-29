# https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python

def cookie(x):
    suf = 'Who ate the last cookie? It was {}!'
    if type(x) == str:
        return suf.format('Zach')
    if type(x) in (float, int):
        return suf.format('Monica')
    return suf.format('the dog')

