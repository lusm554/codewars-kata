# https://www.codewars.com/kata/526989a41034285187000de4/train/python

import ipaddress as ip 

def ips_between(start, end):
    return int(ip.IPv4Address(end)) - int(ip.IPv4Address(start))

