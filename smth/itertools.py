from itertools import count, cycle

seq = count(start=10, step=100)
end = 10 * 100

while next(seq) < end:
    print(next(seq))

clock = cycle([1, 2, 3, 4, 5, 6])
cnt = 0

while cnt != 7:
    print(next(clock))
    cnt+=1
