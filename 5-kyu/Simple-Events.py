# https://www.codewars.com/kata/52d3b68215be7c2d5300022f/train/python

class Event():
    def __init__(self):
        self.callbacks = []
    
    def subscribe(self, func):
        self.callbacks.append(func)
        return self
    
    def unsubscribe(self, func):
        self.callbacks.remove(func)
        return self
    
    def emit(self, *args):
        [func(*args) for func in self.callbacks]
        return self

