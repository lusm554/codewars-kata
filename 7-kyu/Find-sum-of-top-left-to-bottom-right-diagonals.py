# https://www.codewars.com/kata/5497a3c181dd7291ce000700/train/python

def diagonal_sum(a):
    return sum(a[i][i] for i in range(len(a)))

