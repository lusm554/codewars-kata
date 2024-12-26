# https://www.codewars.com/kata/567bed99ee3451292c000025/train/python

import re
def is_vowel(s): 
    return len(s) == 1 and bool(re.match(r'[aeiouAEIOU]', s))
