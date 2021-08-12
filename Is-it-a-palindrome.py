# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

