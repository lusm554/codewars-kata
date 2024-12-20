# https://www.codewars.com/kata/52ea928a1ef5cfec800003ee/train/python

import functools
def ip_to_int32(ip):
    return int.from_bytes([int(x) for x in ip.split('.')], byteorder='big')
