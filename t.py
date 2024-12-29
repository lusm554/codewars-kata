class PokerHand(object):
    def __repr__(self):  return self.hand

    def __init__(self, hand):
        self.hand = hand
        self.rank = 1
  
    def __lt__(self, other):
      return self.rank < other.rank
        
hands = list()
hands.append(PokerHand("KS 2H 5C JD TD"))
hands.append(PokerHand("2C 3C AC 4C 5C"))
hands.sort()
hands = sorted(hands)
print(hands)

