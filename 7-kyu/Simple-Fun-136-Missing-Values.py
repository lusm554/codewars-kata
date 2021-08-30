# https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/python

def missing_values(seq):
    seq = sorted(set([i for i in seq if seq.count(i) in [1, 2]]), key=seq.count)
    return seq[0]**2 * seq[1]

