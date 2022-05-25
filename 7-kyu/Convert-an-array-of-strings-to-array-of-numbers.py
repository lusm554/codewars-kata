# https://www.codewars.com/kata/5783d8f3202c0e486c001d23/train/python

def to_float_array(arr): 
    return list(map(lambda x: float(x) if '.' in x else int(x), arr))

