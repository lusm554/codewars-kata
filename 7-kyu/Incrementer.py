# https://www.codewars.com/kata/590e03aef55cab099a0002e8/train/python

def incrementer(nums):
    return [k+i+1 if (k+i+1) < 10 else (k+i+1) % 10 for k, i in enumerate(nums)]

