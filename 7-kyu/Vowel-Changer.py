# https://www.codewars.com/kata/597754ba62f8a19c98000030/train/python

def vowel_change(txt, vow):
    for i in ['a', 'e', 'i', 'o', 'u']:
        txt = txt.replace(i, vow)
    return txt
