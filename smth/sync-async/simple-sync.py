import time

def f1(x):
    print(x**2)
    time.sleep(3)
    print("f1 done")

def f2(x):
    print(x**0.5)
    time.sleep(3)
    print("f2 done")

def main():
    i = 5
    f1(i)
    f2(i)

print("Start", time.strftime("%X"))
main()
print("End", time.strftime("%X"))


