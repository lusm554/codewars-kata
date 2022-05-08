# https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/python

import re

def hex_string_to_RGB(h): 
    rgb = {k: int(v, 16) for k, v in zip('rgb', re.findall('..', h[1:]))}
    return rgb

