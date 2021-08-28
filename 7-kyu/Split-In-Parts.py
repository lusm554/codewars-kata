# https://www.codewars.com/kata/5650ab06d11d675371000003/train/python

def split_in_parts(s, l):
    return ' '.join(s[i:i+l] for i in range(0, len(s), l))
