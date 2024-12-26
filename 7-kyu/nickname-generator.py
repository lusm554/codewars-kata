# https://www.codewars.com/kata/593b1909e68ff627c9000186/train/python

def nickname_generator(name):
    if len(name) <= 3: return 'Error: Name too short'
    if name[2] in 'aeiou':
        return name[:4]
    return name[:3]
