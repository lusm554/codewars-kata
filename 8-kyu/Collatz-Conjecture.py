# https://www.codewars.com/kata/577a6e90d48e51c55e000217/train/python

def hotpo(n):
    count = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n / 2
        count += 1
    return count

