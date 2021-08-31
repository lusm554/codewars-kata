# https://www.codewars.com/kata/555b73a81a6285b6ce000047/train/python

def add(*a):
    return sum(a[i]*(i+1) for i in range(len(a)))

