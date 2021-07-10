#!/usr/bin/env python3.9
# https://www.codewars.com/kata/5262119038c0985a5b00029f/python

from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

