# https://www.codewars.com/kata/5a4d303f880385399b000001/solutions/python
import math
def strong_num(number):
    if sum(math.factorial(int(d)) for d in str(number)) == number:
        return "STRONG!!!!"
    return "Not Strong !!"
