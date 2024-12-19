# https://www.codewars.com/kata/563f037412e5ada593000114/train/python

def calculate_years(principal, interest, tax, desired):
  y = 0
  balance = principal
  while 1:
    if balance >= desired:
      return y
    income = balance * interest
    income -= income * tax
    balance += income
    y += 1
