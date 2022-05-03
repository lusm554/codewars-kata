# https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python


def most_money(ss):
    r = {s.name: s.fives * 5 + s.tens * 10 + s.twenties * 20 for s in ss}
    if len(r) == 1:
        return next(iter(r))
    ma = max(r, key=r.get)
    mi = min(r, key=r.get)
    return ma if not ma == mi else "all"

