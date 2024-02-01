# https://www.codewars.com/kata/5803956ddb07c5c74200144e/solutions/python

def dating_range(age):
    if age <= 14:
        _min = int(age - .1 * age)
        _max = int(age + .1 * age)
    else:
        _min = int(age/2 + 7)
        _max = int((age-7)*2)
    return f'{_min}-{_max}'
