# https://www.codewars.com/kata/5827acd5f524dd029d0005a4/train/python

def is_ruby_coming(lst):
    return any(i['language'] == 'Ruby' for i in lst)
