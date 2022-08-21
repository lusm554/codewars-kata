#!/usr/bin/env python3

limit = 50
ran = range(limit + 1)

sqsum = sum([x**2 for x in ran])
print(sqsum)

sqsum = (limit * (limit+1) * (2*limit + 1)) / 6
print(sqsum)

