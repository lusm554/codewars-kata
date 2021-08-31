# https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/python

def solve(n):
    if n % 10: return -1
    m = [10, 20, 50, 100, 200, 500]
    count = 0
    for i in m[::-1]:
        count += n // i
        n = n % i
    return count
