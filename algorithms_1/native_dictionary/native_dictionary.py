class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        p = 0.33
        summ = sum(map(lambda s: ord(s) * p, key))
        return int(summ % self.size)

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        self.slots[self.hash_fun(key)] = key
        self.values[self.hash_fun(key)] = value

    def get(self, key):
        return self.values[self.hash_fun(key)] if self.is_key(key) else None
