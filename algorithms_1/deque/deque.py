class Deque:
    def __init__(self):
        self.items = []
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def addFront(self, item):
        self.items.append(item)
        self._size += 1

    def addTail(self, item):
        self.items.insert(0, item)
        self._size += 1

    def removeFront(self):
        if not self.isEmpty():
            self._size -= 1
            return self.items.pop()
        return None

    def removeTail(self):
        if not self.isEmpty():
            self._size -= 1
            item = self.items[0]
            self.items = self.items[1:]
            return item
        return None

    def size(self):
        return self._size
