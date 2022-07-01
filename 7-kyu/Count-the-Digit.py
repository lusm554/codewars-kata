# https://www.codewars.com/kata/566fc12495810954b1000030/solutions/python

def nb_dig(n, d):
    return sum(str(x**2).count(str(d)) for x in range(n+1))

