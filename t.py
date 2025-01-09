# def mul2x2mat(a, b, m): 
#     c = [[0,0], [0,0]]
#     c[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % m 
#     c[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % m 
#     c[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % m 
#     c[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % m 
#     return c

# def pisano_period(m):
#     base_mat = [[0, 1], [1, 1]]
#     one_mat = [[1, 0], [0, 1]]
#     curr_mat = one_mat
#     for k in range(1, m*m+1):
#         curr_mat = mul2x2mat(curr_mat, base_mat, m)
#         if curr_mat == one_mat:
#             return k

from math import gcd
def find_pisano_period_prime(p, exp):
    mod = p**exp
    prev, curr = 0, 1
    for k in range(1, mod * mod + 1):
        prev, curr = curr, (prev + curr) % mod
        if prev == 0 and curr == 1:
            return k

def pisano_period(m):
    def prime_factors(n):
        factors = []
        d = 2
        while d * d <= n:
            exp = 0
            while n % d == 0:
                n //= d
                exp += 1
            if exp > 0:
                factors.append((d, exp))
            d += 1
        if n > 1:
            factors.append((n, 1))
        return factors

    factors = prime_factors(m)
    periods = [find_pisano_period_prime(p, exp) for p, exp in factors]
    
    from functools import reduce
    def lcm(a, b):
        return a * b // gcd(a, b)

    return reduce(lcm, periods)

