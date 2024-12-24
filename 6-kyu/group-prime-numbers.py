# https://www.codewars.com/kata/593e8d839335005b42000097/train/python

def get_primes(n, m=2):
    def primes(cnt):
        i = 2
        while 1:
            if all(i%j != 0 for j in range(2, int(i**.5)+1)):
                yield i
            i += 1
    primeg = primes(n)
    pcnt = 0
    for _ in range(0, n, m):
        group = list()
        for _ in range(m):
            if pcnt == n:
                break
            group.append(next(primeg))
            pcnt += 1
        if len(group) != m:
            group.extend([None]*(m-len(group)))
        yield tuple(group)
        if pcnt == n:
            break
