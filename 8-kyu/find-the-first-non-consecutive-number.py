# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python

def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        frst, scnd = arr[i-1], arr[i]
        if abs(abs(frst) - abs(scnd)) >= 2:
            return scnd
    return None
