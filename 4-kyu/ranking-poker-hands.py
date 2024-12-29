# https://www.codewars.com/kata/5739174624fc28e188000465/train/python

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
    return [c for c in self.cards if c['val'] in card_pairs]
    
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

  def __repr__(self): return f"cards={self.cards!r})"

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
#   if rank == 1:
#     return [hand_cards.cards[-1]], [other_cards.cards[-1]]
  if rank in {2, 3}:
    print(1)
    print( hand_cards.pairs_cards_lst, other_cards.pairs_cards_lst)
    return hand_cards.pairs_cards_lst, other_cards.pairs_cards_lst
  if rank == 4:
    return hand_cards.set_cards, other_cards.set_cards
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

class PokerHand:
    RESULT = ["Loss", "Tie", "Win"]
    def __init__(self, hand):
        self.hand = hand
        
    def compare_with(self, other):
        hand_rank, hand_cards = rank_hand(self.hand)
        other_rank, other_cards = rank_hand(other.hand)
        if hand_rank > other_rank:
            return 'Win'
        elif hand_rank < other_rank:
            return 'Loss'
        else:
            return rank_eq_rank(hand_rank, hand_cards, other_cards)
