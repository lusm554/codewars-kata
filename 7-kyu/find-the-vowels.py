# https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python

def vowel_indices(word):
    return [i + 1 for i in range(len(word)) if word[i].lower() in 'aeiouy']

