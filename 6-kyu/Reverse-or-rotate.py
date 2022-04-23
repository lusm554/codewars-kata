# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python

def revrot(s, sz):
    if sz == 0: return ''
    
    res = ''
    l = int(len(s)/sz)
    
    for i in range(0, l*sz, sz):
        chunk = s[i: i+sz]
        if sum(map(lambda x: int(x)**3, chunk)) % 2 == 0:            
            res += chunk[::-1]
        else:
            res += chunk[1:] + chunk[:1]
    
    return res

