# https://www.codewars.com/kata/581214d54624a8232100005f/train/python

def matrix(lst):
    ln = len(lst)   
    return [[lst[i][j] if i != j else 0 if lst[i][j] < 0 else 1 for j in range(ln)] for i in range(ln)]

