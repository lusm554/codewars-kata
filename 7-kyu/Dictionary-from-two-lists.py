# https://www.codewars.com/kata/5533c2a50c4fea6832000101/train/python

def createDict(k, v):
    v = v[:len(k)]
    return dict(zip(k, v+([None]*(len(k)-len(v)))))

