# https://www.codewars.com/kata/598106cb34e205e074000031/train/python

def count_deaf_rats(town):
    left, right = town.replace(' ', '').strip().split('P')
    split_2c = lambda s: [s[i:i+2] for i in range(0, len(s), 2)] 
    left, right = split_2c(left), split_2c(right)
    res = left.count('O~') + right.count('~O')
    return res
