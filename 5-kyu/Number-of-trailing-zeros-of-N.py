# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/

def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


# TEST
print(zeros(0) == 0)
print(zeros(6) == 1)
print(zeros(30) == 7)
