import time

# machine - 2.3 GHz IC i5, memory 8 GB 2133 MHz DDR3, graphics Intal Irus Plus
# 640 1536 MB

# my version of fibonacci 
def fib(n, start=[0, 1]): 
    res = []
    a, b, *_ = start 
    for i in range(n):
        res.append(a)
        a, b = b, b+a
    return res

s1 = time.time()
#fib(10**5) # 0.3950619697570801
fib(35) # 9.059906005859375e-06
print(time.time() - s1)

# divide and conquer approach
def dqFib(n):
    if n < 2: return 1
    return dqFib(n - 1) + dqFib(n - 2)

s = time.time()
#dqFib(10**5) # RecursionError: maximum recursion depth exceeded in comparison
dqFib(35) # 3.3280160427093506
print(time.time() - s)

mem = {} # how get fib nums? mem.values()
# dynamic approach 
def dFib(n):
    if n in mem: return mem[n]
    f = 0
    if n < 2:
        f = 1
    else:
        f = dFib(n - 1) + dFib(n - 2)

    mem[n] = f
    return f
s2 = time.time()
dFib(35) # 3.1948089599609375e-05 
print(time.time() - s2)

