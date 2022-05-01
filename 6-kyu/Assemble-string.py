# https://www.codewars.com/kata/6210fb7aabf047000f3a3ad6/train/python

def assemble(arr):
    d = {}
    for s in arr:
        for i in range(len(s)):
            c = s[i]
            
            if not c == '*':
                d[i] = c
            elif c == '*' and not i in d:
                d[i] = '#'
            

    return ''.join(v for k, v in d.items())


