# https://www.codewars.com/kata/538835ae443aae6e03000547/train/python

def add(n):
    def _add(num):
        return num + n
    return _add
