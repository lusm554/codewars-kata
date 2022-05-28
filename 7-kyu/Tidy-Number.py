# https://www.codewars.com/kata/5a87449ab1710171300000fd/train/python

def tidyNumber(n):
    ns = []
    while n != 0:
        ns.append(n%10)
        n//=10
    ns = ns[::-1]
    
    for i in range(len(ns)-1):
        if not ns[i] <= ns[i+1]:
            return False
    return True

