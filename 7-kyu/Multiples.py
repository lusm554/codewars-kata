# https://www.codewars.com/kata/55a8a36703fe4c45ed00005b/train/python

def multiple(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'BangBoom'
    if x % 3 == 0:
        return 'Bang'
    if x % 5 == 0:
        return 'Boom'
    return 'Miss'

