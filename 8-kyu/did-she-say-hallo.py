# https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python

def validate_hello(greetings):
    greetings = greetings.lower()
    grts = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any(sub in greetings for sub in grts)
