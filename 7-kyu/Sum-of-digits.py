# https://www.codewars.com/kata/59cf805aaeb28438fe00001c/train/python

# short solution
def sum_of_digits(d):
    return '' if d is None else f"{' + '.join(str(d))} = {sum(map(int, str(d)))}"

# more readable solution

def sum_of_digits2(d):
    if d is None: return ''
    d = str(d)
    return f"{' + '.join(d)} = {sum(map(int, d))}"

