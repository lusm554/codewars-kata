class queue:


    def __init__(sefl):
        self.MAX_LEN = 10
        self.data = []
    

    def length(self):
        return len(self.data)


    def enque(self, item):
        if len(sefl.data) < MAX_LEN:
            return self.data.append(item)
        else:
            raise OverflowError()

    
    def deque(self):
        if len(self.data) == 0:
            raise IndexError()
        else:
            self.data.pop(0)
