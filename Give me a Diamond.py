# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python

def diamond(n):
    if n % 2 == 0 or n < 0: return None
    
    half = [['*'*j for j in [1]*x] for x in range(-1, n+1, 2) if x!=-1]
    full = [*half[:len(half)-1], half[len(half)-1], *half[:len(half)-1][::-1]]
    
    result = ''
    for row in full:
        sp_count = (n - len(row))//2
        result = result + ' '*sp_count + ''.join(row) + '\n'
    return result

print(diamond(45))
