# https://www.codewars.com/kata/547274e24481cfc469000416/train/python

class Human:
    @property
    def greetings(self):
        return f"Hello! My name is {self.name}."

class Man(Human):
    def __init__(self, name="Adam"):
        self.name = name

class Woman(Human):
    def __init__(self, name="Eve"):
        self.name = name
    

def God():
    return [Man(), Woman()]
   
