# https://www.codewars.com/kata/56419475931903e9d1000087/train/python

def one_down(txt):
    if str != type(txt): return "Input is not a string"
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    encoded = "ZABCDEFGHIJKLMNOPQRSTUVWXYzabcdefghijklmnopqrstuvwxy"
    caesar = str.maketrans(table, encoded)
    result = txt.translate(caesar)
    return result
