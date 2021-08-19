# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

def count_positives_sum_negatives(a):
    return [
        sum([1 if x > 0 else 0 for x in a]),
        sum(x if x < 0 else 0 for x in a)
    ] if a else []

