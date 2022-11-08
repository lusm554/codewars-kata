class Series:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

def main():
    lst = Series(1, 10)
    for i in lst:
        print(i)

if __name__ == "__main__":
    main()
