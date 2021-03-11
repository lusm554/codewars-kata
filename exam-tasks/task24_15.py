# https://inf-ege.sdamgia.ru/problem?id=27699

st = open('zadanie24_2.txt', 'r').readlines()[0]
kmax = 0

j = st.find('LDR')
k = 0

while j < len(st) :
    if st[j : j + 3] == 'LDR' :
        k += 3
        j += 2
    elif k :
        if st[j : j + 2] == 'LD' :
            k += 2
            j += 1
        elif st[j] == 'L' :
            k += 1
        kmax = max(k,kmax)
        k = 0
    j += 1

print(kmax)
