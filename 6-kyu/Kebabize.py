# https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python

import re

def kebabize(s):
    filtered = [c for c in re.split('(?=[A-Z])', ''.join(c for c in s if c.isalpha())) if c.isalpha()]
    
    return '-'.join(filtered).lower()

