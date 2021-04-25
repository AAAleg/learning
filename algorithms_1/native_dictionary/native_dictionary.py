class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        ratio = 0.33
        total_sum = sum(map(lambda s: ord(s) * ratio, key))
        return int(total_sum % self.size)

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        self.slots[self.hash_fun(key)] = key
        self.values[self.hash_fun(key)] = value

    def get(self, key):
        return self.values[self.hash_fun(key)] if self.is_key(key) else None
