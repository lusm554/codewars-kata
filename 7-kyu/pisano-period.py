# https://www.codewars.com/kata/5f1360c4bc96870019803ae2/train/python

def pisano(n):
    curr = 0
    next = 1
    period = 0
    while 1:
        prev_next = next
        next = (curr + next) % n
        curr = prev_next
        period += 1 
        if curr == 0 and next == 1:
            return period
