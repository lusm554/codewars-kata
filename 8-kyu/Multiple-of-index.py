# https://www.codewars.com/kata/5a34b80155519e1a00000009/train/python

def multiple_of_index(arr):
    return [arr[x] for x in range(1, len(arr)) if arr[x] % x == 0]

