# https://www.codewars.com/kata/58d76854024c72c3e20000de/train/python

def reverse_alternate(s):
    s = s.split(' ')
    s = [x for x in s if x]
    return ' '.join(w.strip()[::-1] if i % 2 != 0 else w.strip() for i, w in enumerate(s))

