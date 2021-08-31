# https://www.codewars.com/kata/582746fa14b3892727000c4f/train/python

def count_developers(lst):
    return sum(1 for i in lst if i['language'] == 'JavaScript' and i['continent'] == 'Europe')

