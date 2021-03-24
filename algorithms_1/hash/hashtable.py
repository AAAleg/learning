class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(map(ord, value)) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        count = 0

        while None in self.slots:
            if self.slots[index] is None:
                return index
            if self.slots[index] is not None:
                index += self.step
            if index > self.size - 1:
                index = count
                count += 1
        
        return None

    def put(self, value):
        index = self.seek_slot(value)

        if index is not None:
            self.slots[index] = value
            return index
        else: 
            return None

    def find(self, value):
        count = 0
        index = self.hash_fun(value)
        while value in self.slots:
            if self.slots[index] == value:
                return index
            if self.slots[index] != value:
                count += self.step
            if index > self.size - 1:
                index = count 
                count += 1
        else:
            return None
