# https://www.codewars.com/kata/580755730b5a77650500010c/train/python

def sort_my_string(s):
    odd_ch = ""
    even_ch = ""
    for i in range(len(s)):
        if i % 2 == 0:
            even_ch += s[i]
        else:
            odd_ch += s[i]
    return f"{even_ch} {odd_ch}"

def sort_my_string(s):
    return '{} {}'.format(s[::2], s[1::2])

