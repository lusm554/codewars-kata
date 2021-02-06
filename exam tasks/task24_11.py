f = open('zadanie24_2.txt', 'r')
s = f.readline()

m = 1
k = 1

for i in range(1, len(s)):
  if s[i] != s[i-1]:
    k += 1
  else:
    k = 1
  m = max(m, k)

print(m)
