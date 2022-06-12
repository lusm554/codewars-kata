# https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python

def array(s):
    s = s.split(',')
    if len(s) < 3: 
        return None
    
    return " ".join(s[1:len(s)-1])

