# https://www.codewars.com/kata/55b051fac50a3292a9000025/train/python

def filter_string(string):
    return int(''.join(filter(str.isdigit, string)))

