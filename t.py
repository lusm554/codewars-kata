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

  @functools.cached_property
  def pairs_cards_lst(self):
    card_pairs = [val for val, cnt in self.val_count.items() if cnt == 2]
    print(f"{card_pairs=}")
    res = [c for c in self.cards if c['val'] in card_pairs] 
    print(f"{res=}")
    return res

  @functools.cached_property
  def set_cards(self):
    try:
      card_set = next(val for val, cnt in self.val_count.items() if cnt == 3)
      return [c for c in self.cards if c['val'] == card_set]
    except StopIteration:
      return list()

  @functools.cached_property
  def fok_cards(self):
    try:
      card_set = next(val for val, cnt in self.val_count.items() if cnt == 4)
      return [c for c in self.cards if c['val'] == card_set]
    except StopIteration:
      return list()

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
      return rank, cards

def get_cards_by_rank(rank, hand_cards, other_cards):
  #if rank == 1:
    #return [hand_cards.cards[-1]], [other_cards.cards[-1]]
  if rank in {2, 3}:
    return hand_cards.pairs_cards_lst, other_cards.pairs_cards_lst
  if rank == 4:
    return hand_cards.set_cards, other_cards.hand_cards
  if rank == 8:
    return hand_cards.fok_cards, other_cards.fok_cards
  #5, 6, 7, 9, 10
  return hand_cards.cards, other_cards.cards

def rank_eq_rank(rank, hand_cards, other_cards):
  print(f"{rank=}")
  hcards, ocards = get_cards_by_rank(rank, hand_cards, other_cards)
  hcards = sorted(hcards, key=lambda x: (x['val'], x['suit']), reverse=True)
  ocards = sorted(ocards, key=lambda x: (x['val'], x['suit']), reverse=True)
  for hc, oc in zip(hcards, ocards):
    print(f"{hc=} {oc=}")
    if hc['val'] > oc['val']:
      return 'Win'
    elif hc['val'] < oc['val']:
      return 'Loss'
  _hcards = sorted(hand_cards.cards, key=lambda x: (x['val'], x['suit']), reverse=True)
  _ocards = sorted(other_cards.cards, key=lambda x: (x['val'], x['suit']), reverse=True)
  for hc, oc in zip(_hcards, _ocards):
    print(f"{hc=} {oc=}")
    if hc['val'] > oc['val']:
      return 'Win'
    elif hc['val'] < oc['val']:
      return 'Loss'
  return 'Tie'
  
def compare_hand(hand, other):
  print(f"{hand=} {other=}")
  hand_rank, hand_cards = rank_hand(hand)
  other_rank, other_cards = rank_hand(other)
  if hand_rank > other_rank:
    return 'Win'
  elif hand_rank < other_rank:
    return 'Loss'
  else:
    return rank_eq_rank(hand_rank, hand_cards, other_cards)

def run_test(name, shouldbe, hand, other):
  res = compare_hand(hand, other)
  if res == shouldbe:
    print('\033[92m' + f"\t{name} {res=} {shouldbe=}" + '\033[0m')
  else:
    print('\033[91m' + f"\t{name} {res=} {shouldbe=}" + '\033[0m')


run_test("1",        "Win", "JC 4S 6S 4H 9H", "KC AC 3C 8S 3D")
run_test("Highest straight flush wins",        "Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
run_test("Straight flush wins of 4 of a kind", "Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD")
run_test("Highest 4 of a kind wins",           "Win",  "AS AH 2H AD AC", "JS JD JC JH 3D")
run_test("4 Of a kind wins of full house",     "Loss", "2S AH 2H AS AC", "JS JD JC JH AD")
run_test("Full house wins of flush",           "Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H")
run_test("Highest flush wins",                 "Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")
run_test("Flush wins of straight",             "Win",  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C")
run_test("Equal straight is tie",              "Tie",  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S")
run_test("Straight wins of three of a kind",   "Win",  "2S 3H 4H 5S AD", "AH AC 5H 6H AS")
run_test("3 Of a kind wins of two pair",       "Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS")
run_test("2 Pair wins of pair",                "Win",  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S")
run_test("Highest pair wins",                  "Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S")
run_test("Pair wins of nothing",               "Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")
run_test("Highest card loses",                 "Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")
run_test("Highest card wins",                  "Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC")
run_test("Equal cards is tie",               "Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")

'''
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
'''
