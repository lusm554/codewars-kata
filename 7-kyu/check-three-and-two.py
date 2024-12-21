# https://www.codewars.com/kata/5a9e86705ee396d6be000091/train/python

def check_three_and_two(arr):
    return len(set(arr)) == 2 and arr.count(arr[0]) in {2, 3}
