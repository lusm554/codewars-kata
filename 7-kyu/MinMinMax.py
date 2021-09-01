# https://www.codewars.com/kata/58d3487a643a3f6aa20000ff/train/python

def minMinMax(arr):
    return [min(arr), min(i for i in range(min(arr), max(arr)) if i not in arr), max(arr)]

