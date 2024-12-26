# https://www.codewars.com/kata/557af4c6169ac832300000ba/train/python

def remove_rotten(bag_of_fruits):
    if not bag_of_fruits: return []
    return [w.replace('rotten', '').lower() for w in bag_of_fruits]
