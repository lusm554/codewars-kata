# https://inf-ege.sdamgia.ru/problem?id=29672

f = open('inf_22_10_20_24.txt') # file from link with task

counter = 0

for i in f:
  E = i.count('E')
  A = i.count('A')
  if E > A: counter += 1

print(counter) # 467
