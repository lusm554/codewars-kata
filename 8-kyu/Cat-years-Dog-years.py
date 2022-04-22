# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(hy):
    r = lambda x, y: (15 if i == 0 else 9 if i == 1 else y for i in range(x))
    return [hy, sum(r(hy, 4)), sum(r(hy, 5))]

