#!/usr/bin/env python3.9
# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

def two_sum(nums, t):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == t and i != j:
                return [i, j]

# TEST
class Test:
    def assert_equals(self, val, expect):
        print(val == expect)

test = Test()
test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])
