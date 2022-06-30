# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python

def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    return f"Oi! Sheep number {len(queue)-queue.index('wolf')-1}! You are about to be eaten by a wolf!"

