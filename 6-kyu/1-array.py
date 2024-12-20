# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python

def up_array(arr):
    if len(arr) == 0 or any(x < 0 or x > 9 for x in arr): return
    if arr == [0]: return [1]
    zeros_before = ''
    for x in arr:
        if x == 0: zeros_before +='0'
        else: break
    return [int(x) for x in zeros_before + str(int(''.join(str(x) for x in arr)) + 1)]
