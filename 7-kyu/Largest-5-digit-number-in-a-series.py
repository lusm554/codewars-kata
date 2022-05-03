# https://www.codewars.com/kata/51675d17e0c1bed195000001/train/python

def solution(d):
    m = d[:5]
    ism = lambda x, y: int(x) > int(y)
    for i in range(len(d)):
        if i == len(d)-4:
            break
        c = d[i: i+5]
        if ism(c, m):
            m = c
    return int(m)

