# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

from collections import Counter 
import re

def top_3_words(text):
    ptrn = re.compile("(?=.*\w)^(\w|')+$")
    text = text.lower()
    text = text.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    text = (x for x in text.split(' ') if x != '')
    text = filter(lambda x: bool(ptrn.match(x)) if "'" in x else True, text)
    return [x[0] for x in Counter(text).most_common(3)]
