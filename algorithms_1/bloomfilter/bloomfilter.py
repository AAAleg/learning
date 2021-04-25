class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.slots = [0] * f_len

    def hash1(self, str1):
        result = 0
        for c in str1:
            code = ord(char)
            result = ((result * 17) + code) % self.filter_len
        return result

    def hash2(self, str1):
        result = 0
        for char in str1:
            code = ord(char)
            result = ((result * 223) + code) % self.filter_len
        return result

    def add(self, str1):
        self.slots[self.hash1(str1)] = 1
        self.slots[self.hash2(str1)] = 1

    def is_value(self, str1):
        if self.slots[self.hash1(str1)] == 1 and self.slots[self.hash2(str1)] == 1:
            return True
        else:
            return False
