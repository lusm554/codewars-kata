# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

def tribonacci(signature, n):
    if n == 0: return []
    
    a, b, c = signature
    result = []
    for i in range(n):
        result.append(a)
        a, b, c = b, c, a+b+c
    return result
    
print(tribonacci([3, 2, 1], 10))
# [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
