import functools
import collections

v2i = {
  'T': 10,
  'J': 11,
  'Q': 12,
  'K': 13,
  'A': 14,
}
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

  @functools.cached_property
  def val(self): return [c['val'] for c in self.cards]

  @functools.cached_property
  def suit(self): return [c['suit'] for c in self.cards]

  @functools.cached_property
  def unique_suit(self): return set(self.suit)

  @functools.cached_property
  def val_count(self): return dict(collections.Counter(self.val))

  def __repr__(self): return f"Cards(hand={self.hand!r})"

def rank_hand(hand):
  cards = Cards(hand)

  def is_card_seq(cards):
    stepsize_one = lambda s: not any((x2 - x1) != 1 for x1, x2 in zip(s, s[1:]))
    seq_to_check = [cards.val]
    if v2i['A'] in cards.val:
      seq = sorted([1 if x == v2i['A'] else x for x in cards.val]) # low ace condition
      seq_to_check.append(seq)
    return any(stepsize_one(seq) for seq in seq_to_check)

  flush_royal = lambda c: c.val[0] == 10 and is_card_seq(c) and len(c.unique_suit) == 1
  straight_flush = lambda c: is_card_seq(c) and len(c.unique_suit) == 1
  four_of_kind = lambda c: 4 in c.val_count.values()
  full_house = lambda c: len(c.val_count) == 2 and 3 in c.val_count.values() and 2 in c.val_count.values()
  flush = lambda c: len(c.unique_suit) == 1
  straight = lambda c: is_card_seq(c)
  three_of_kind = lambda c: 3 in c.val_count.values() # set
  two_pair = lambda c: list(c.val_count.values()).count(2) == 2 # double set
  one_pair = lambda c: list(c.val_count.values()).count(2) == 1 # set
  high_card = lambda c: c.cards[-1]

  combinations_order = [
    flush_royal,
    straight_flush,
    four_of_kind,
    full_house,
    flush,
    straight,
    three_of_kind,
    two_pair,
    one_pair,
    high_card,
  ]

  names = [
    'flush royal', 'straight flush', 'for of kind', 'full house', 'flush',
    'straight', 'three of kind', 'two pair', 'one pair', 'high card'
  ]
  for comb, name, rank in zip(combinations_order, names, range(len(combinations_order), 0, -1)):
    r = comb(cards)
    if r:
      return rank
    '''
    if r:
      print('\033[92m' + f"\t{name} {r} {rank}" + '\033[0m')
    else:
      print('\t', name, r, rank)
    '''

def compare_hand(hand):
  hand_rank = rank_hand(hand)
  print(hand_rank)

# SHDC
hands = [
 ('TS JS QS KS AS', 'flush royal'),# flush royal
 ('4S 5S 6S 7S 8S', 'straight flush'), # straight flush
 ('2S 3S 4S 5S AS', 'straight flush low ace'), # straight flush low ace
 ('TS 5S 5H 5C 5D', 'four of a kind'), # four of a kind
 ('JS JD KH KC KD', 'full house'), # full house
 ('6S 8S QS 3S TS', 'flush'), # flush
 ('6S 7D 8S 9C TH', 'straight'), # straight
 ('2S 3D 4S 5C AH', 'straight low ace'), # straight low ace
 ('KD 8S KS KC TS', 'three of kind / set'), # three of kind / set
 ('4S 8S 4D 7C 8H', 'two pair'), # two pair
 ('3S 3D 1D TC 2H', 'one pair'), # one pair
 ('2S 3D 5D 8C TH', 'high card'), # high card
]

for hand, sol in hands:
  print(hand, sol)
  compare_hand(hand)
  print()
