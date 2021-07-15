import time

# just factorial here
def fact(n):
    f = 1
    for n in range(1, n+1):
        f *= n
    return f

start = time.time()
for kill_my_cpu in range(1, 10*100):
    print(fact(kill_my_cpu))

print('\nso, {} seconds!'.format(time.time() - start))
