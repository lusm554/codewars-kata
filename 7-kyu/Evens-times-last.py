# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python

def even_last(n): 
    return sum(n[i]*n[-1] for i in range(len(n)) if i % 2 == 0)

