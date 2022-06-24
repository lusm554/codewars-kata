# https://www.codewars.com/kata/5753b987aeb792508d0010e2/train/python

def every(lst, N=0, strt=0):
    lst = lst[strt:]
    if N == 0:
        return lst
    return [lst[i] for i in range(0, len(lst), N)]

