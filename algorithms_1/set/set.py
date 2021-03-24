class HashTable:
    def __init__(self, sz, stp):
        self._size = sz
        self.step = stp
        self.slots = [None] * self._size

    def hash_fun(self, value):
        p = 0.33
        summ = sum(map(lambda s: ord(s) * p, value))
        return int(summ % self._size)

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


class PowerSet(HashTable):

    def __init__(self):
        super().__init__(20000, 3)

    def size(self):
        return len([slot for slot in self.slots if slot])

    def put(self, value):
        if value not in self.slots:
            super().put(value)

    def get(self, value):
        return True if self.find(value) else False

    def remove(self, value):
        if value in self.slots:
            self.slots.remove(value)
            return True
        return False

    def intersection(self, set2):
        result = PowerSet()

        for item in self.slots:
            if item and set2.get(item):
                result.put(item)

        return result 

    def union(self, set2):
        result = PowerSet()
        for item in self.slots + set2.slots:
            result.put(item)
        return result

    def difference(self, set2):
        result = PowerSet()
        for item in self.slots:
            if item and not set2.get(item):
                result.put(item)
        return result

    def issubset(self, set2):
        for item in set2.slots:
            if item and not self.get(item):
                return False
        return True
