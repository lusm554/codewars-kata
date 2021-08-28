# https://www.codewars.com/kata/59e49b2afc3c494d5d00002a/train/python

def sort_vowels(s):
    if not isinstance(s, str): return ''
    vowels = 'aeiouAEIOU'
    return '\n'.join(f'|{i}' if i in vowels else f'{i}|' for i in s)
