# https://www.codewars.com/kata/55a14aa4817efe41c20000bc/train/python

from preloaded import Animal

class Cat(Animal):
    def speak(self):
        return f'{self.name} meows.'
