# https://www.codewars.com/kata/59564f3bcc15b5591a00004a/train/python

def filter_even_length_words(words):
    return list(filter(lambda w: len(w) % 2 == 0, words))

