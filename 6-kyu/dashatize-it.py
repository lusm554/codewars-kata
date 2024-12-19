# https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
def dashatize(n):
  res = ''
  for d in str(abs(n)):
    if int(d) % 2 != 0:
      res += f'-{d}-'
    else:
      res += d
  res = res.replace('--', '-').strip('-')
  return res
