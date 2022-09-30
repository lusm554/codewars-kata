import datetime

def timeit(unit="s"):
    def decorator(f):
        def wrap(*args):
            start = datetime.datetime.now()
            f(*args)
            stop = datetime.datetime.now()
            d = stop - start
            match unit:
                case "h":
                    dd = d.total_seconds()/3600
                case "m":
                    dd = d.seconds/60
                case "s":
                    dd = d.seconds
                case "ms":
                    dd = d.microseconds 
            print(f"Done in: {dd}{unit}")
        return wrap
    return decorator

@timeit(unit="h")
def fibo(n):
    a, b = 1, 1
    for i in range(n):
        #print(a)
        a, b = b, a + b

fibo(13**5)
