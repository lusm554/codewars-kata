# https://www.codewars.com/kata/57a37f3cbb99449513000cd8/train/python

def get_number_from_string(s):
    return int(''.join(i for i in s if i.isdigit()))

