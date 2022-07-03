# https://www.codewars.com/kata/5877786688976801ad000100/train/python

from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

def words_to_object(s):
    try:
        res = []
        for name, id in chunk(s.split(" "), 2):
            c = {
                "name": name,
                "id": id
            }
            c = f"{{name : '{name}', id : '{id}'}}"
            res.append(c)

        return f"[{', '.join(res)}]"
    except:
        return "[]"
    
