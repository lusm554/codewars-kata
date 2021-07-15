import time

def very_slow_method():
    s = 0
    for i in range(10**11):
        s += i
    return s

def fast_method():
    N = 10**11
    s = N * (N + 1) / 2
    return s

start1 = time.time()
print(fast_method())
print(time.time() - start1, 'seconds')

start2 = time.time()
# print(very_slow_method())
print('too many minutes')
