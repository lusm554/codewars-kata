# https://www.codewars.com/kata/56a32dd6e4f4748cc3000006/train/python

def get_vals(town, s):
    s = [ts.split(':')[-1] for ts in s.split('\n') if town == ts[:ts.index(":")]]
    if not s:
        return None
    s = s[0]
    vals = [float(v[4:]) for v in s.split(',')]
    return vals

def mean(town, s):
    town_vals = get_vals(town, s)
    if not town_vals:
        return -1
    return sum(town_vals) / len(town_vals)

def variance(town, s):
    import numpy as np
    town_vals = get_vals(town, s)
    if not town_vals:
        return -1
    return np.var(town_vals)
