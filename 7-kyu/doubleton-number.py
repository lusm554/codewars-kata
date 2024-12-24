# https://www.codewars.com/kata/604287495a72ae00131685c7/train/python

def doubleton(num):
    check = lambda n: len(set(str(n))) == 2
    num += 1
    while not check(num):
        num += 1
    return num
