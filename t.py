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
        print(self.hand)
        print(self.value_cnts)
  
    def __lt__(self, other):
      return self.rank < other.rank
        
hands = list()
hands.append(PokerHand("KS 2H 5C JD TD"))
hands.append(PokerHand("2C 3C AC 4C 5C"))
hands.sort()
hands = sorted(hands)
print(hands)

