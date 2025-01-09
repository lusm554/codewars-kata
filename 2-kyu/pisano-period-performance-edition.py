# https://www.codewars.com/kata/65de16794ccda6356de32bfa/train/python
import random

SMALL_PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
]

# Детерминированные основания для Miller-Rabin (64-bit)
MR_BASES_64 = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

_prime_cache = {}
_factor_cache = {}
_pisano_prime_cache = {}

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime_64(n):
    if n < 2:
        return False
    if n in _prime_cache:
        return _prime_cache[n]
    for sp in SMALL_PRIMES:
        if sp == n:
            _prime_cache[n] = True
            return True
        if n % sp == 0 and n != sp:
            _prime_cache[n] = False
            return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d >>= 1
        r += 1
    for a in MR_BASES_64:
        if a >= n:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            _prime_cache[n] = False
            return False
    _prime_cache[n] = True
    return True

def trial_division(n):
    for p in SMALL_PRIMES:
        if p * p > n:
            break
        while n % p == 0:
            yield p
            n //= p
    if n > 1:
        yield n

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    while True:
        x = random.randrange(2, n - 1)
        c = random.randrange(1, n - 1)
        f = lambda v: (v*v + c) % n
        y = x
        d = 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
            if d == n:
                break
        if d > 1 and d < n:
            return d

def factor(n):
    if n in _factor_cache:
        return _factor_cache[n]
    if n < 2:
        _factor_cache[n] = []
        return []
    if is_prime_64(n):
        _factor_cache[n] = [n]
        return [n]
    # Сначала "малая" факторизация
    res = []
    tmp = n
    for p in SMALL_PRIMES:
        if p * p > tmp:
            break
        while tmp % p == 0:
            res.append(p)
            tmp //= p
    if tmp == 1:
        _factor_cache[n] = sorted(res)
        return _factor_cache[n]
    if is_prime_64(tmp):
        res.append(tmp)
    else:
        d = pollard_rho(tmp)
        res += factor(d)
        res += factor(tmp // d)
    _factor_cache[n] = sorted(res)
    return _factor_cache[n]

def divisors_from_factorization(facts):
    # строим все делители (комбинаторика по степеням)
    from collections import Counter
    c = Counter(facts)
    items = list(c.items())
    divs = [1]

    for (p, e) in items:
        new_divs = []
        for d in divs:
            cur = 1
            for _ in range(e+1):
                new_divs.append(d*cur)
                cur *= p
        divs = new_divs
    return sorted(divs)

def fib_mod_fast_doubling(n, m):
    if n == 0:
        return (0, 1)
    a, b = fib_mod_fast_doubling(n >> 1, m)
    c = (a*((b << 1) - a)) % m
    d = (a*a + b*b) % m
    if n & 1:
        return (d, (c + d) % m)
    else:
        return (c, d)

def legendre_5(p):
    if p == 5:
        return 0
    ls = pow(5, (p-1)//2, p)
    if ls == 1:
        return 1
    if ls == p-1:
        return -1
    return 0

def pisano_prime(p):
    if p in _pisano_prime_cache:
        return _pisano_prime_cache[p]
    if p == 2:
        _pisano_prime_cache[p] = 3
        return 3
    if p == 5:
        _pisano_prime_cache[p] = 20
        return 20
    ls = legendre_5(p)
    if ls == 1:
        fct = factor(p-1)
    else:
        fct = factor(2*(p+1))
    divs = divisors_from_factorization(fct)
    for d in divs:
        f0, f1 = fib_mod_fast_doubling(d, p)[0], fib_mod_fast_doubling(d+1, p)[0]
        if f0 == 0 and f1 == 1:
            _pisano_prime_cache[p] = d
            return d
    _pisano_prime_cache[p] = None
    return None

def pisano_prime_power(p, k):
    if k == 1:
        return pisano_prime(p)
    if p == 2:
        if k == 2:
            return 6
        if k == 3:
            return 12
        return 3*(2**(k-1))
    if p == 5:
        return 20*(5**(k-1))
    return (p**(k-1)) * pisano_prime(p)

def pisano_period(n):
    if n < 2:
        return 1
    from collections import Counter
    fcts = factor(n)
    cnt = Counter(fcts)
    vals = []
    for p, e in cnt.items():
        vals.append(pisano_prime_power(p, e))
    def lcm(a, b):
        return a//gcd(a,b)*b
    r = 1
    for v in vals:
        r = lcm(r, v)
    return r
