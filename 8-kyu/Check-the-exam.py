# https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

def check_exam(a1, a2):
    s = sum([4 if a1[i]==a2[i] else 0 if a2[i]=='' else -1 for i in range(len(a1))])
    return s if s > 0 else 0

