import time

# some list
l = [7, 6, 1, 5, 4, 3]



def bubble(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


s = time.time()
sorted(l)
print('built-in sorted', time.time() - s)

s = time.time()
bubble(l)
print('bubble sort', time.time() - s)
