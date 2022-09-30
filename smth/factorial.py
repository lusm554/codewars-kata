"""
fact = 10
n = 1
# factorial of 10 == 3.628.800

for i in range(1, fact + 1):
    n *= i

print(n)
"""

# simple recursive
def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)


#res = fact(500)
#print(res)

# recursion with memoize
_fact_cache = {}
def mem_fact(n):
    if n == 1:
        return n
    res = _fact_cache.get(n)
    if res is None:
        res = n * mem_fact(n-1)
        _fact_cache[n] = res
    return res

#res = mem_fact(500)
#print(res)

from functools import lru_cache

# or with lru_cache
@lru_cache()
def fact_wdec(n):
    if n == 1:
        return n
    return n * fact(n-1)

res = fact_wdec(500)
print(res)

