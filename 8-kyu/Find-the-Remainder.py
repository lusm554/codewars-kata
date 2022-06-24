# https://www.codewars.com/kata/524f5125ad9c12894e00003f/train/python


def remainder(a, b):
    a, b = sorted([a, b])
    return None if a == 0 else b % a

