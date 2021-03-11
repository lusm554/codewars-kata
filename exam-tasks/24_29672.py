# https://inf-ege.sdamgia.ru/problem?id=29672

f = open('inf_22_10_20_24.txt', 'r')

counter = 0

def fs(sym, string):
  count = 0
  for i in string:
    if i == sym:
      count += 1
  return count

for line in f:
  if fs('A', line) < fs('E', line):
    counter += 1

print(counter)
