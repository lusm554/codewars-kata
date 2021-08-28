# https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python

def remove_duplicate_words(s):
    res = []
    for w in s.split(' '):
        if w in res: continue
        res.append(w)
    return ' '.join(res)
