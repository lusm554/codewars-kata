# https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python

from collections import defaultdict
def is_solved(board):
    lines = [*board]
    diag, other_diag = list(), list()
    cols = defaultdict(list)
    for i in range(len(board)):
        diag.append(board[i][i])
        other_diag.append(board[i][len(board)-i-1])
        for j, v in enumerate(board[i]):
            cols[j].append(v)
    lines.extend([diag, other_diag, *cols.values()]) 
    for l in lines:
        sl = set(l)
        if sl == {1}:
            return 1
        if sl == {2}:
            return 2
    if any(0 in l for l in lines):
        return -1
    return 0
