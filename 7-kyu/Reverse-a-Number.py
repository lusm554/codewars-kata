# https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python

def reverse_number(num):
    num = str(num)
    if num[0] == '-':
        num = num[1:]
        return int(num[::-1]) * -1
    return int(num[::-1])

