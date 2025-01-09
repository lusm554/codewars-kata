# Very slow
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


# Little bit faster
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

# More faster, bot not enough
def pisano_period_prime_power(p, k):
    """
    Функция для нахождения периода Пизано для числа p^k
    """
    # Специальный метод для чисел вида p^k, где p - простое число
    n = p ** k
    previous, current = 0, 1
    for i in range(0, n * n):
        previous, current = current, (previous + current) % n
        if previous == 0 and current == 1:
            return i + 1
    return None

def pisano_period_prime(n):
    """
    Функция для нахождения периода Пизано для простого числа n
    """
    previous, current = 0, 1
    for i in range(0, n * n):
        previous, current = current, (previous + current) % n
        if previous == 0 and current == 1:
            return i + 1

def lcm(a, b):
    """
    Функция для нахождения НОК (наименьшее общее кратное)
    """
    from math import gcd
    return a * b // gcd(a, b)

def prime_factors(n):
    """
    Функция для разложения числа на простые множители
    """
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def pisano_period(n):
    """
    Основная функция для нахождения периода Пизано для составного числа N
    """
    factors = prime_factors(n)
    periods = []
    
    # Для каждого простого множителя вычисляем его период Пизано
    for factor in set(factors):
        count = factors.count(factor)
        if count > 1:
            # Если это степень простого числа, используем специальный метод
            periods.append(pisano_period_prime_power(factor, count))
        else:
            # Если это просто простое число, используем стандартный метод
            periods.append(pisano_period_prime(factor))
    
    # Возвращаем НОК всех периодов Пизано для простых множителей
    period = periods[0]
    for p in periods[1:]:
        period = lcm(period, p)
    return period

