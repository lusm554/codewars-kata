# https://www.codewars.com/kata/5547929140907378f9000039/train/python

import re

def shortcut(s):
    return re.sub("[aeiou]", "", s)

