# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.rank_ord = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def next_rank(self):
        try:
            self.rank = self.rank_ord[self.rank_ord.index(self.rank)+1] 
        except IndexError:
            pass
        
    def inc_progress(self, rank):
        if rank not in self.rank_ord:
            raise ValueError(rank)
        if self.rank == self.rank_ord[-1]:
            return
        urank_pos = self.rank_ord.index(self.rank)
        prank_pos = self.rank_ord.index(rank)
        if urank_pos == prank_pos:
            self.progress += 3
        elif prank_pos > urank_pos:
