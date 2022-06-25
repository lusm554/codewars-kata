# https://www.codewars.com/kata/629049687438580064f0e6dd/train/python


import itertools as it

def encode(nonogram):
    axisn = lambda n: tuple(tuple(len(list(iter)) for key, iter in it.groupby(sub) if key == 1) for sub in n)
    return (axisn(zip(*nonogram)), axisn(nonogram))

