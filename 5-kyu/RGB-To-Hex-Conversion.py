# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

def rgb(*rgb):
    r, g, b = [i if i in range(0, 256) else [0, 255][i > 0] for i in rgb]
    return  f"{r << 16 | g << 8 | b:06x}".upper()

