# https://www.codewars.com/kata/5ac49156376b11767f00060c/train/python

# not the best practice
def alternate_sort(l):
    n = sorted([i for i in l if i < 0], reverse=True)
    p = sorted(i for i in l if i >= 0)
    b = len(n) if len(n) > len(p) else len(p)
    res = []
    for i in range(b):
        if not i > len(n)-1:
            res.append(n[i])
        if not i > len(p)-1:
            res.append(p[i])
    return res
