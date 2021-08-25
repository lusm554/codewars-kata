# https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python

def string_clean(s):
    return ''.join(filter(lambda x: not x.isdigit(), list(s)))

