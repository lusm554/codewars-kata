# https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/solutions/python

def even_numbers(arr, n):
    return list(filter(lambda x: x % 2 == 0, arr))[::-1][:n][::-1]

