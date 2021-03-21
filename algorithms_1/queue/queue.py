class Queue:
    def __init__(self):
        self.items = []
        self._size = 0

    def isEmpty(self):
    	return self._size == 0

    def enqueue(self, item):
        self.items.insert(0, item)
        self._size += 1

    def dequeue(self):
        if not self.isEmpty():
        	self._size -= 1
        	return self.items.pop()
        return None 

    def size(self):
        return self._size

    def rotate(self, n):
    	if not self.isEmpty():
    		for _ in range(n):
    			self.enqueue(self.dequeue())
