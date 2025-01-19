# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python

def rot13(msg):
    basic = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    encoded = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    rot13 = str.maketrans(basic, encoded)
    result = msg.translate(rot13)
    return result
