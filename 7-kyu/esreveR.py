# https://www.codewars.com/kata/5413759479ba273f8100003d/train/python

def reverse(lst):
    empty_list = list()
    for i in range(len(lst)-1, -1, -1):
        empty_list.append(lst[i])
    return empty_list
    
