# https://www.codewars.com/kata/5a651865fd56cb55760000e0

def array_leaders(numbers):
    return [n for (i,n) in enumerate(numbers) if n>sum(numbers[(i+1):])]

