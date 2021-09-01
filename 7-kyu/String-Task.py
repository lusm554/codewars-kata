# https://www.codewars.com/kata/598ab63c7367483c890000f4/train/python

def string_task(s):
    v = 'aoyeui'
    return ''.join('' if i in v else f'.{i}' for i in s.lower())
