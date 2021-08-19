def lh(l):
    # min
    mi = l[0]
    # max
    ma = l[0]
    for num in l:
        if num < mi:
            mi = num
        if num > ma:
            ma = num
    return [mi, ma]


# TEST
print(lh([4, 2, 5, 2, 1, 32, 10, 6, 14]) == [1, 32])
print(lh([-1, -2, 5, 2, 1, 35, 2, -3, 100]) == [-3, 100])
print(lh([-3, -35, -23, -6, -3, -7, -34]) == [-35, -3])

