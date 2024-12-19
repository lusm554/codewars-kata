# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python
def title_case(title, minor_words=''):
  title = iter(title.lower().split(' '))
  minor_words = minor_words.lower().split(' ')
  title_res = next(title).capitalize()
  for w in title:
    if w in minor_words: title_res += ' ' + w.lower()
    else: title_res += ' ' + w.capitalize()
  return title_res
