# https://www.codewars.com/kata/53f1015fa9fe02cbda00111a/train/python

from random import choice

class Ghost(object):
    def __init__(self):
        self.color = choice(["white", "yellow", "purple", "red"])

