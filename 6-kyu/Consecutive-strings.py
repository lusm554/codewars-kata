# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    n = len(strarr)
    maxelem = ""
    if n == 0 or k > n or k <= 0:
        return ""
    
    lsts = [strarr[i:] for i in range(k)]  
    for i in zip(*lsts):
        i = "".join(i)
        if len(i) > len(maxelem):
            maxelem = i
    return maxelem

