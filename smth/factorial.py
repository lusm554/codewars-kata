"""
fact = 10
n = 1
# factorial of 10 == 3.628.800

for i in range(1, fact + 1):
    n *= i

print(n)
"""

def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)


res = fact(500)
print(res)

