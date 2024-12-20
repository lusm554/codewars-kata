# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

def sum_pairs(ints, s):
  seen = set()
  for num in ints:
    if (s - num) in seen:
      return [s - num, num]
    seen.add(num)
