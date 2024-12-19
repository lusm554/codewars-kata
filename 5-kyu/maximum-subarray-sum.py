# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

# Kadane's algorithm
def max_sequence(arr):
  if all(n < 0 for n in arr): return 0
  if all(n > 0 for n in arr): return arr
  max_sum = float('-inf')
  current_sum = 0
  for n in arr:
    current_sum = max(n, current_sum + n)
    max_sum = max(max_sum, current_sum)
  return max_sum

# out of time
'''
from collections import defaultdict
def max_sequence(arr):
  if all(n < 0 for n in arr): return 0
  if all(n > 0 for n in arr): return arr
  max_sum = float('-inf')
  max_sum_arr = []
  for win_size in range(1, len(arr)+1):
    for sub in [arr[i:i+win_size] for i in range(0, len(arr), 1)]:
      if sum(sub) > max_sum:
        max_sum = sum(sub)
  return max_sum
'''
