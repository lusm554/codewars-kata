# https://www.codewars.com/kata/5aff237c578a14752d0035ae/train/python

from math import sqrt, floor

def predict_age(*age):
    return floor(sqrt(sum([i*i for i in age]))/2)
    
