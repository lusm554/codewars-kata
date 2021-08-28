# https://www.codewars.com/kata/53daa9e5af55c184db00025f/train/python

def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True
