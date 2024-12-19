# https://www.codewars.com/kata/5375f921003bf62192000746/train/python

import string
def abbreviate(s):
  print(s)
  word = ''
  encoded = ''
  def encode_word(word):
    if len(word) >= 4:
      return f"{word[0]}{len(word)-2}{word[-1]}"
    return word 
  for ch in s:
    if ch not in string.ascii_letters:
      encoded += encode_word(word) 
      encoded += ch
      word = ''
    else:
      word += ch
  encoded += encode_word(word) 
  return encoded

