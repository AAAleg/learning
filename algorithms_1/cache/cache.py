class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        p = 0.33
        result = sum(map(lambda s: ord(s) * p, key))
        return int(result % self.size)

    def is_key(self, key):
        return key in self.slots

    def seek_slot(self, value):
        index = self.hash_fun(value)
        step = 3

        while True:
            try:
                if None not in self.slots:
                    remove_index = self.hits.index(min(self.hits))
                    self.hits[remove_index] = 0
                    self.slots[remove_index] = None
                    self.values[remove_index] = None
                if self.slots[index] == None:
                    return index
                if self.slots[index] != None:
                    index += step
            except IndexError:
                index = 0
                step //= 2

    def put(self, key, value):
        index = self.seek_slot(value)
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] += 1

    def get(self, key):
        if self.is_key(key):
            index = self.hash_fun(key)
            self.hits[index] += 1
            return self.values[index]  
        else:
            None