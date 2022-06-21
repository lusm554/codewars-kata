# https://www.codewars.com/kata/619f200fd0ff91000eaf4a08/train/python

def odd_or_even(n):
    if n % 2 == 0:
        if n//2 % 2 == 0:
            return "Even"
        return "Odd"
    return "Either"

