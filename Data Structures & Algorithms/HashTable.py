# The Hash table ds stores items in key-value pairs where
# key   - unique integer that is used for indexing the values
# value - data that are associated with keys.
# In a hash table, a new index is processed using the keys. And, the item
# corresponding to that key is stored in the index. This process is called
# hashing.

from math import sqrt
from itertools import count, islice
from random import randint

class HashTable:
    def __init__(self, size):
        self.hash = [[]] * size

    def insert(self, key, val):
        index = self.__tohash__(key)
        self.hash[index] = [key, val]

    def remove(self, key):
        index = self.__tohash__(key)
        self.hash[index] = []

    def __tohash__(self, key):
        capacity = self.__getPrime__(10)
        return key % capacity

    def __getPrime__(self, n):
        if n % 2 == 0: return n + 1
        while not self.__isPrime__(n):
            n += 2
        return n

    def __isPrime__(self, n):
        return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

if __name__ == '__main__':
    # TEST
    h = HashTable(100)
    keys = [randint(1, 1000) for i in range(100)]        
    values = [randint(1, 1000) for i in range(100)]
    for k, v in zip(set(keys), set(values)):
        h.insert(k, v)
    print(h.hash)
