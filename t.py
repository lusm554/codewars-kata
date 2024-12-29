from collections import Counter
class Card:
  def __init__(self, card):
    self.value = int({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(card[0], card[0])) 
    self.suit = card[1]

class PokerHand:
    def __repr__(self):  return self.hand

    def __init__(self, hand):
        self.hand = [Card(card) for card in hand.split()]
        self.value_cnts = Counter(card.value for card in self.hand)

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
        return
  
    def __lt__(self, other):
      return self.rank < other.rank
        
hands = list()
hands.append(PokerHand("KS 2H 5C JD TD"))
hands.append(PokerHand("2C 3C AC 4C 5C"))
hands.sort()
hands = sorted(hands)
print(hands)

