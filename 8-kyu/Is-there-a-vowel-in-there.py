# https://www.codewars.com/kata/57cff961eca260b71900008f/train/python

def is_vow(inp):
    sym = list(map(ord, ['a', 'e', 'i', 'o', 'u']))
    return [chr(i) if i in sym else i for i in inp]

