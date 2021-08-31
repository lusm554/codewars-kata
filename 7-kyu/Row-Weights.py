# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python

def row_weights(a):
    t1, t2 = [0], [0]
    for i in range(len(a)):
        t1.append(a[i]) if i % 2 == 0 else t2.append(a[i])
    return (sum(t1), sum(t2))
