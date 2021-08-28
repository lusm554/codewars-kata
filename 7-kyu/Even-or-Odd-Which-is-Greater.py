# https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python

def even_or_odd(s):
    e, o = sum(int(i) for i in s if int(i)%2==0), sum(int(i) for i in s if int(i)%2 != 0)
    if e > o:
        return 'Even is greater than Odd'
    if o > e:
        return 'Odd is greater than Even'
    return 'Even and Odd are the same'
