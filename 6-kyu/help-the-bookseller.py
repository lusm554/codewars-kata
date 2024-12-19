# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

def stock_list(stocklist, categories):
  if len(stocklist) == 0 or len(categories) == 0: return ''
  cats = {c: list() for c in categories}
  for s in stocklist:
    cat, cnt = s.split(' ')
    cat, cnt = cat[0], int(cnt)
    if cat not in cats: continue
    cats[cat].append(cnt)
  return ' - '.join(f'({c} : {sum(v)})' for c, v in cats.items())
