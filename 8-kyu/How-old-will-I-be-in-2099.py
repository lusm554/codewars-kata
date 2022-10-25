# https://www.codewars.com/kata/5761a717780f8950ce001473/train/python

def calculate_age(birth, curr):
    diff = abs(birth-curr)
    unit = "year" if diff==1 else "years"
    if birth < curr:
        msg = f"You are {diff} {unit} old."
    elif birth > curr:
        msg = f"You will be born in {diff} {unit}."
    else:
        msg = f"You were born this very year!"
    return msg

