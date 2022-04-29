# https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python

def whatday(num):
    if not num in range(1, 8): return "Wrong, please enter a number between 1 and 7"
    d = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return {i: s for i, s in zip(range(1, 8), d)}[num]

