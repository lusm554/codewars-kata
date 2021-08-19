# https://www.codewars.com/kata/58dced7b702b805b200000be/train/python

# formula for Distance between points √[(x₂ - x₁)² + (y₂ - y₁)²]
from math import sqrt

def distance_between_points(a, b):
    x1, y1 = a.x, a.y
    x2, y2 = b.x, b.y
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

