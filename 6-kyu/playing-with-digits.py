# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
  dsum = 0
  for d in str(n):
    dsum += int(d)**p
    p += 1
  if dsum % n == 0:
    return dsum / n
  return -1
