# https://www.codewars.com/kata/58f0ba42e89aa6158400000e/train/python

def fold_to(dist):
    if dist < 0: return None
    if dist == 0: return 0
    cnt = 0
    i = 0.0001
    while i < dist:
        i*=2
        cnt+=1
    return cnt


