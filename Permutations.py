#!/usr/bin/env python3.9
# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

from itertools import permutations as pr

def permutations(s):
    l = [''.join(x) for x in list(pr(list(s)))]
    return list(set(l))


#-------TEST---------
class Test:
    def assert_equals(self, v, sh):
        print(v==sh)

test = Test()
test.assert_equals(sorted(permutations('a')), ['a']);
test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
