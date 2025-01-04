# https://www.codewars.com/kata/59031db02b0070a923000110/train/python

zero_or_one=lambda n,s:[sum(l)>n//2 for l in zip(*s)]

# too large
zero_or_one=lambda n,s:[max(l,key=l.count)for l in zip(*s)]
