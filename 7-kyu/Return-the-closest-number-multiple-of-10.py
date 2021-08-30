# https://www.codewars.com/kata/58249d08b81f70a2fc0001a4/train/python

def closest_multiple_10(i):
    return i//10 * 10 if i%10 < 5 else i//10 * 10 + 10

