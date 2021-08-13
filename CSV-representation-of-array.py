# https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/train/python

def to_csv_text(a):
    return '\n'.join([','.join(map(str, x)) for x in a])

