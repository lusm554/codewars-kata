# https://www.codewars.com/kata/594adadee075005308000122/train/python

def even_and_odd(n):
    n = str(n)
    res = ['', '']
    for i in n:
        if int(i) % 2 == 0:
            res[0] += i
        else:
            res[1] += i
    return tuple(map(lambda x: 0 if x == '' else int(x), res))
