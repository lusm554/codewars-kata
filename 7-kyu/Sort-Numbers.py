# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python

def solution(n):
    if not n: return []
    for i in range(len(n)):
        for j in range(i, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
    return n

def solution2(n):
    return sorted(n) if n else []

print(solution([1, 3, 2, 6]))

