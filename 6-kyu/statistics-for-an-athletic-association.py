# https://www.codewars.com/kata/55b3425df71c1201a800009c/train/python

import pandas as pd
import time
def stat(strg):
  if strg == '': return ''
  df = pd.DataFrame([r.split('|') for r in strg.split(',')], columns=list('hms')).astype(int)
  df['total_sec'] = df.h * 3600 + df.m * 60 + df.s
  df = df.total_sec.agg([lambda lst: max(lst) - min(lst), 'mean', 'median'])
  df = df.apply(lambda sec: time.strftime('%H|%M|%S', time.gmtime(sec)))
  report = ' '.join(f"{lbl}: {res}" for lbl, res in zip(['Range', 'Average', 'Median'], df.values))
  return report
