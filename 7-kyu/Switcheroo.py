# https://www.codewars.com/kata/57f759bb664021a30300007d/train/python

def switcheroo(s):
    return ''.join(map(lambda x: x if x not in 'ab' else 'a' if x=='b' else 'b', s))

