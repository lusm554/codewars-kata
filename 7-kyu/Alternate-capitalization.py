# https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python

def capitalize(s):
    s = ''.join(sym if i%2 else sym.upper() for i, sym in enumerate(s))
    return [s, s.swapcase()]

