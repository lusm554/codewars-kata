import time
import random

def s(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

# test time, best case and worst case

# best case
t = list(range(1, 1001))
start = time.time()
#print(s(t))
s(t)
print(time.time() - start)

# worst case
t = list(range(1000, 0, -1))
start = time.time()
#print(s(t))
s(t)
print(time.time() - start)

# some random values
t = [random.randint(1, 10**10000) for i in range(1000 * 5)]
start = time.time()
s(t)
print(time.time() - start)
