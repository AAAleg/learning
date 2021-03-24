class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        p = 0.33
        summ = sum(map(lambda s: ord(s) * p, value))
        return int(summ % self.size)

    def seek_slot(self, value):
        index = self.hash_fun(value)
        step = self.step

        if None in self.slots:
            i = self.hash_fun(value)
            step = self.step

            while True:
                try:
                    if self.slots[index] is None:
                        return index
                    else:
                        index += step
                except IndexError:
                    index = 0
                    step //= 2
        else:
            return None

    def put(self, value):
        index = self.hash_fun(value)

        if self.slots[index] is None:
            self.slots[index] = value
            return index

        elif None in self.slots:
            index = self.seek_slot(value)
            self.slots[index] = value
            return index
        else:
            return None

    def find(self, value):
        index = self.hash_fun(value)

        if self.slots[index] == value:
            return index
        else:
            try:
                index = self.slots.index(value)
                return index
            except ValueError:
                return None
