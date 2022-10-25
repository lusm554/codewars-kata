# https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/python

def find_smallest(nums, to_return):
    return min(nums) if to_return == 'value' else nums.index(min(nums))

