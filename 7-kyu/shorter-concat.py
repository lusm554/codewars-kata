# https://www.codewars.com/kata/54557d61126a00423b000a45/train/python

def shorter_reverse_longer(a,b):
    if len(a) == len(b):
        return b + a[::-1] + b
    short = a if len(a) < len(b) else b
    long = a if len(a) > len(b) else b
    return short + long[::-1] + short
