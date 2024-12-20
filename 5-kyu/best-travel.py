# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python
import itertools
def choose_best_sum(t, k, ls):
    dists = set()
    for towns_dist in itertools.combinations(ls, k):
        if sum(towns_dist) <= t:
            dists.add(sum(towns_dist))
    if len(dists) == 0: return
    return sorted(dists, reverse=True)[0]
