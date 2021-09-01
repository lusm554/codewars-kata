# https://www.codewars.com/kata/564ab935de55a747d7000040/train/python

def remove(text, what):
    for char, count in what.items():
        text = text.replace(char, '', count)
    return text
