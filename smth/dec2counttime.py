import time

def timeit(f):
    def wrap(*args):
        start = time.time()
        f(*args)
        stop = time.time()
        print("Done in:", stop-start)
    return wrap

@timeit
def fibo(n):
    a, b = 1, 1
    for i in range(n):
        #print(a)
        a, b = b, a + b

fibo(10**6)
