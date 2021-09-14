# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

# realy good solution
def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]

# ...
def multiplication_table(s):
    res = [[j if i == 1 else i for j in range(1, s+1)] for i in range(1, s+1)]
    for i in range(1, s):
        for j in range(1, s):
             res[i][j] = res[0][j] * res[i][0]
    return res
