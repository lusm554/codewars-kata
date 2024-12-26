# https://www.codewars.com/kata/5939ab6eed348a945f0007b2/train/python

def longest_word(s):
    s = s.split(' ')
    return s[s.index(max(s[::-1], key=lambda x: len(x)))]
