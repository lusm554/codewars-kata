# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

from ipaddress import IPv4Address, AddressValueError

def is_valid_IP(s):
    try:
        IPv4Address(s)
        return True
    except AddressValueError:
        return False

