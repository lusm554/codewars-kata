# https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python

def calc(s):
    total1 = "".join(str(ord(x)) for x in s)
    total2 = total1.replace("7", "1")
    return sum(int(x) for x in total1) - sum(int(x) for x in total2)

