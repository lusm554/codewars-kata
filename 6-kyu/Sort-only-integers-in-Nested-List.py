# https://www.codewars.com/kata/5a4bdd73d8e145f17d000035/train/python

def sort_nested_list(ar):
    a, b, c = len(ar), len(ar[0]), len(ar[0][0])
    if not c: return [[[]]]
    res = []
    for i in ar:
        for j in i:
            for k in j:
                res.append(k)
    res.sort()
    res = [res[i: i+c] for i in range(0, len(res), c)]
    return [res[j: j+b] for j in range(0, len(res), b)]
