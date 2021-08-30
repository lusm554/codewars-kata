# https://www.codewars.com/kata/5546180ca783b6d2d5000062/solutions/python

# simple solution
def squares(x, n):
    res = []
    for i in range(n):
        if len(res) == 0:
            res.append(x)
        else:
            res.append(res[i-1]**2)
    return res

# one line solution
def squares2(x,n):
    return [x**(2**i) for i in range(n)]
