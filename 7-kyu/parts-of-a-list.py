# https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python
def partlist(arr):
    res = list()
    for i in range(1, len(arr)):
        r = tuple([' '.join(arr[:i]), ' '.join(arr[i:])])
        res.append(r)
    return res
