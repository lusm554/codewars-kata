# https://www.codewars.com/kata/5effa412233ac3002a9e471d/train/python

import numpy as np

def add(num1, num2):
    n1, n2 = sorted([num1, num2])

    n1 = list(map(lambda x: int(x), str(n1)))
    n2 = list(map(lambda x: int(x), str(n2)))

    a1 = np.array(n1)
    a2 = np.array(n2)

    a1 = np.insert(a1, [0] * (len(a2)-len(a1)), 0)
    res = a1 + a2

    return int("".join(str(x) for x in res))

