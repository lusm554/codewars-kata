# https://www.codewars.com/kata/53d32bea2f2a21f666000256/train/python
def largest(n, xs):
  """Find the n highest elements in a list"""
  return sorted(xs)[len(xs)-n:]
