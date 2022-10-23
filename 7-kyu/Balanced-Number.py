# https://www.codewars.com/kata/5a4e3782880385ba68000018/train/python

def balanced_num(n):
    n = str(n)
    m = len(n)//2
    if len(n) % 2 == 0:
        lh = n[0:m-1]
        rh = n[m+1:]
    else:
        lh = n[0:m]
        rh = n[m+1:]
    sum_half = lambda s: sum(int(x) for x in s)
    return "Balanced" if sum_half(lh) == sum_half(rh) else "Not Balanced"
        
