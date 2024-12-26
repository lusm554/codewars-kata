# https://www.codewars.com/kata/57ee24e17b45eff6d6000164/train/python

def cat_mouse(x):
    if x.strip('.').count('.') <= 3:
        return "Caught!"
    return "Escaped!"
