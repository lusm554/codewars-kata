import math

def myrange(start, stop=None, step=1):
    if not (type(start) == int and
            type(stop) in [int, type(None)] and
            type(step) == int):
        raise ValueError("where it my ints?")

    if start and stop is None:
        stop = start
        start = 0
    
    cnt = 0
    limit = abs(start - stop)
    while cnt < limit:
        yield start
        start += step
        cnt +=1


for i in myrange(0, 10):
    print(i, end=' ')
print()

for i in myrange(10):
    print(i, end=' ')
print()

for i in range(10):
    print(i, end=' ')
print()

for i in myrange(10, 0, -1):
    print(i, end=' ')
print()

for i in range(10, 0, -1):
    print(i, end=' ')
print()
