# https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python

def how_much_i_love_you(n):
    return ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all'][((n + 6) % 6)-1]

