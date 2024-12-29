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
        print(self.rank)

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
        return (7, get_by_cnt(4), get_by_cnt(1))


      return -1, None
  
    @property
    def sort_rank(self):
      return self.rank[0]

    def __lt__(self, other):
      return self.sort_rank < other.sort_rank
        
hands = list()
hands.append(PokerHand("KS 2H 5C JD TD"))
hands.append(PokerHand("2C 3C AC 4C 5C"))
hands.sort()
hands = sorted(hands)
print(hands)

