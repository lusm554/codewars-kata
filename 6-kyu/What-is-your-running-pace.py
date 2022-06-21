# https://www.codewars.com/kata/578b8c0e84ac69a4d20004c8/train/python

from math import floor

def running_pace(dist, time):
    comm_s = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
    s_pers_k = comm_s//dist
    return f"{int(s_pers_k//60)}:{floor(s_pers_k%60):02d}"   

