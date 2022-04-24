# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

def validBraces(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}','')
        s = s.replace('[]','')
        s = s.replace('()','')
    return s == ''

