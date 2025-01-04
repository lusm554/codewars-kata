# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

import itertools
def get_pins(observed):
    n2dpossible = {
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '6', '8', '4'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8'],
        '0': ['0', '8'],
    }
    chars_per_n = [n2dpossible.get(ch) for ch in observed]
    combs = [''.join(c) for c in itertools.product(*chars_per_n)]
    return combs
