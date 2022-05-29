# https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python

def parse(data):
    i = 0
    r = []
    f = {
        'i': lambda x: x+1,
        'd': lambda x: x-1,
        's': lambda x: x**2,
        'o': lambda x: r.append(x)==None and x
    }
    
    for j in data:
        print(i, r)
        i = f.get(j, lambda x: x)(i)
    return r
    
