# https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d/train/python

def halving_sum(n):
    s = n
    while n > 0:
        s += n//2
        n //= 2
    return s
