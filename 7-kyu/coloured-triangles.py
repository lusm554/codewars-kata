# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/python

def triangle(row):
    if len(row) == 1: return row
    nrow = ''
    triple = set('RGB')
    for i in range(len(row)-1):
        a, b = row[i], row[i+1]
        pair = set(a+b)
        if len(pair) == 1:
            nrow += a
        else:
            nrow += (triple - pair).pop()
    nrow = triangle(nrow)
    return nrow
