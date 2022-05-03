# https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python

def parts_sums(ls):
    rsum = sum(ls)
    lsum = 0 
    r = []
    
    for i in ls+[0]:
        r.append(rsum - lsum)
        lsum += i
    return r

