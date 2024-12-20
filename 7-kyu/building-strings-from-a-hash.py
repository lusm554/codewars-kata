# https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2/train/python
def solution(pairs):
    return ','.join(f"{k} = {v}" for k,v in pairs.items())
