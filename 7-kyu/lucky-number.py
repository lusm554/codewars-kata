# https://www.codewars.com/kata/55afed09237df73343000042/train/python

def is_lucky(n):
    return sum(map(int, str(n))) == 0 or n % 9 == 0
