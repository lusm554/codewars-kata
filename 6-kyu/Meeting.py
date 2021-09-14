# https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python

def meeting(s):
    return "".join(sorted(["({}, {})".format(i[1].upper(),i[0].upper()) for i in [n.split(":") for n in s.split(";")]]))

