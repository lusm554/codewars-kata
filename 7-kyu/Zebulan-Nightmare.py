# https://www.codewars.com/kata/570fd7ad34e6130455001835/train/python

def zebulans_nightmare(s):
    s = s.split('_')
    return s[0] + ''.join(i.title() for i in s[1:])

