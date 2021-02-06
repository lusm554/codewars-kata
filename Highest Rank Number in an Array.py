# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python

def highest_rank(arr):
  counter = {}
  
  for i in set(arr):
    counter[i] = arr.count(i)
 
  maxv = max(counter.values())
  return max([j[0] for j in filter(lambda i: i[1] == maxv, counter.items())])

