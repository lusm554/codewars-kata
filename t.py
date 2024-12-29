from collections import Counter
class Card:
  def __init__(self, card):
    self.value = int({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(card[0], card[0])) 
    self.suit = card[1]

class PokerHand:
    def __repr__(self): return self.src_hand

    def __init__(self, hand):
        self.src_hand = hand
        self.hand = [Card(card) for card in hand.split()]
        self.value_cnts = Counter(card.value for card in self.hand)
        print(f"{self.src_hand=} {self.rank=}")

    @property
    def rank(self):
      def is_flush():
        return len({c.suit for c in self.hand}) == 1

      def is_straight():
        def is_one_increa(seq):
          return all(b-a == 1 for a,b in zip(seq, seq[1:]))
        vals = sorted(c.value for c in self.hand)
        return is_one_increa(vals) or (is_one_increa(vals[:4]) and vals[0] == 2 and vals[-1] == 14) # for low ace
      
      def is_straight_flush():
        return is_flush() and is_straight()

      def is_n_of_kind(n):
        return n in self.value_cnts.values()

      def is_full_house():
        return is_n_of_kind(3) and is_n_of_kind(2)

      def is_2_pair():
        return list(self.value_cnts.values()).count(2) == 2

      def get_by_cnt(n):
        sorted_value_cnts = sorted(self.value_cnts.items(), key=lambda x: (x[1], -x[0]))
        return tuple(val for val, cnt in sorted_value_cnts if cnt == n)
 
      if is_straight_flush():
        return (9, get_by_cnt(1))
      if is_n_of_kind(4):
        return (8, get_by_cnt(4), get_by_cnt(1))
      if is_full_house():
        return (7, get_by_cnt(3), get_by_cnt(2))
      if is_flush():
        return (6, get_by_cnt(1))
      if is_straight():
        return (5, get_by_cnt(1))
      if is_n_of_kind(3):
        return (4, get_by_cnt(3), get_by_cnt(1))
      if is_2_pair():
        return (3, get_by_cnt(2), get_by_cnt(1))
      if is_n_of_kind(2):
        return (2, get_by_cnt(2), get_by_cnt(1))
      return (1, get_by_cnt(1))
  
    @property
    def sort_rank(self):
      #return self.rank[0]
      return self.rank

    def __lt__(self, other):
      return self.sort_rank < other.sort_rank
        
SORTED_POKER_HANDS = list(map(PokerHand, ["KS AS TS QS JS",
                                          "2H 3H 4H 5H 6H",
                                          "AS AD AC AH JD",
                                          "JS JD JC JH 3D",
                                          "2S AH 2H AS AC",
                                          "AS 3S 4S 8S 2S",
                                          "2H 3H 5H 6H 7H",
                                          "2S 3H 4H 5S 6C",
                                          "2D AC 3H 4H 5S",
                                          "AH AC 5H 6H AS",
                                          "2S 2H 4H 5S 4C",
                                          "AH AC 5H 6H 7S",
                                          "AH AC 4H 6H 7S",
                                          "2S AH 4H 5S KC",
                                          "2S 3H 6H 7S 9C"]))

