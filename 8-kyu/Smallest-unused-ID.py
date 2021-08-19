# https://www.codewars.com/kata/55eea63119278d571d00006a/train/python

def next_id(arr):
    if not 0 in arr: return 0
    for i in sorted(arr):
        if i+1 not in arr:
            return i+1

