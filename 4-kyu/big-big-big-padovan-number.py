# https://www.codewars.com/kata/5819f1c3c6ab1b2b28000624/train/python

def mmul(A, B):
    size = len(A)
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                res[i][j] += A[i][k] * B[k][j]
    return res

def mexp(matrix, power):
    size = len(matrix)
    res = [[1 if i==j else 0 for j in range(size)] for i in range(size)]
    base = matrix
    while power:
        if power % 2 == 1:
            res = mmul(res, base)
        base = mmul(base, base)
        power //= 2
    return res

def padovan(n):
    if n in {0, 1, 2}:
        return 1
    tm = [
        [0, 1, 1],
        [1, 0, 0],
        [0, 1, 0],
    ]
    resm = mexp(tm, n-2)
    initv = [1, 1, 1]
    pn = sum(resm[0][i] * initv[i] for i in range(3))
    return pn
