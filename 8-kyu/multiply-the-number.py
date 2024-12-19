# https://www.codewars.com/kata/5708f682c69b48047b000e07/train/python

def multiply(n):
  return n * (5 ** len(str(n).replace('-', '')))
