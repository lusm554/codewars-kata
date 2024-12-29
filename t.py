'''
1. Parse input cards
2. rank hand by combinations condition
3. compatre rank current and other hand
4. return str
'''

v2i = {
  'T': 10,
  'J': 11,
  'Q': 12,
  'K': 13,
  'A': 14,
}

hand = "KS 2H 5C JD TD"
#hand = "AS 2H 5C JD TD" # low ace seq false
#hand = "AS 2H 4C 3D 5D" # low ace seq true
print(hand)

class Cards:
  def __init__(self, hand):
    self.hand = hand
    self.cards = self.parse_hand(hand)
  
  def parse_hand(self, hand):
    cards = [
      {'val': int(v2i.get(c[0], c[0])), 'suit': c[1]} for c in hand.split(' ')
    ]
    cards = sorted(cards, key=lambda x: (x['val'], x['suit']), reverse=False)
    return cards

  @property
  def val(self): return [c['val'] for c in self.cards]

  @property
  def suit(self): return [c['suit'] for c in self.cards]

  def __repr__(self): return f"Cards(hand={self.hand!r})"

from pprint import pp
cards = Cards(hand)
print(cards)
print(cards.val)
print(cards.suit)


def is_card_seq(cards):
  stepsize_one = lambda s: not any((x2 - x1) != 1 for x1, x2 in zip(s, s[1:]))
  seq_to_check = [cards.val]
  if v2i['A'] in cards.val:
    seq = sorted([1 if x == v2i['A'] else x for x in cards.val]) # low ace condition
    seq_to_check.append(seq)
  print('seq',seq_to_check)
  return any(stepsize_one(seq) for seq in seq_to_check)

print(is_card_seq(cards))

exit()

flush_royal = lambda c: c.val[0] == 10 and stepsize_one(c.val) and len(set(c.suit)) == 1
straight_flush = lambda c: stepsize_one(c.val) and len(set(c.suit)) == 1
four_of_kind = None # kare
full_house = None
flush = None
straight = None
three_of_kind = None # set
two_pair = None # double set
one_pair = None # set
high_card = None

combinations_order = [
  flush_royal,
]

for comb in combinations_order:
  print(comb(cards))

'''
card = {
  value 2-10+J Q K A or 1(A)-10+J Q K # low ace
  suit - S H D C

class Card:
  value 2 - 10 11(J) 12(Q) 13(K) 14(A)
  suit - S/H/D/C
  max card
  arr of set card
  set card
  seq

combinations = [
  1. max card val
  2. set - 2 cards with same value
  3. double pairs - set and set
  4. set - 3 cards with same value 
  5. strit - seq values f(n)=n+1
  6. flash - set(suit) == 1
  7. full house - pair and set
  8. care - 4 cards with same value 
  9. strit flash - seq values f(n)=n+1 and len(set(suit)) == 1
 10. flash royal - values 10-A and len(set(suit)) == 1
]
'''

