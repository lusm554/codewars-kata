# https://www.codewars.com/kata/5a092d9e46d843b9db000064/train/python

def solve(arr):
    return [i for i in arr if not (i * -1) in arr][0]

