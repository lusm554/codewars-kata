# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    word = word.lower()
    return "".join(["(" if word.count(c) <= 1 else ")" for c in word])

