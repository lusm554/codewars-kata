# https://inf-ege.sdamgia.ru/problem?id=27698

f = open('zadanie24_2.txt', 'r')

maxc = 0
count = 0
is_last_ok = False

for i in f.readline():
  if i == 'R':  
    if is_last_ok:
      count += 1
    else:
      count = 1
      is_last_ok = True
  else:
    count = 0
    is_last_ok = False
  maxc = max([maxc, count])

print(maxc)
