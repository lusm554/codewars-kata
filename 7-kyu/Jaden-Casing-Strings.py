# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

def to_jaden_case(string):
    return " ".join(x.capitalize() for x in string.split(" "))

