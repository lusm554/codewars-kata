# https://www.codewars.com/kata/5af15a37de4c7f223e00012d/train/python

def men_from_boys(arr):
    even = set()
    odd = set() 
    for i in arr:
        if i % 2 == 0:
            even.add(i)
        else:
            odd.add(i)
    return sorted(even) + sorted(odd, reverse=True)
