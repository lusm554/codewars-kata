# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

# not complete
def next_bigger(n):
    s = sorted(list(str(n)), key=int)
    s.reverse()
    if int(''.join(s)) == n: return -1
    n = str(n)
    # reverse loop through n
    for i in range(len(n)-1, 0, -1):
        f, s = n[i-1], n[i]
        if s > f:
            n = list(n)
            n[i], n[i-1] = f, s
            return int(''.join(n))

# full solution
import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1


# TEST
class Test:
    def assert_equals(self, res, expect):
        print(res==expect)

test = Test()
test.assert_equals(next_bigger(12),21)
test.assert_equals(next_bigger(111),-1)
test.assert_equals(next_bigger(513),531)
test.assert_equals(next_bigger(2017),2071)
test.assert_equals(next_bigger(414),441)
test.assert_equals(next_bigger(144),414)
