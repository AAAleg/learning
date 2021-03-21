import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        if new_capacity < 16:
            new_capacity = 16
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        self.array = self.array[:i] + [itm] + self.array[i:self.count]
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        self.array = self.array[:i] + self.array[i+1:self.count]
        self.count -= 1

        if self.count / self.capacity * 100 < 50:
            self.resize(int(self.capacity / 1.5))


class Stack:
    def __init__(self):
        self.stack = DynArray()
        self.cursor = 0

    def isEmpty(self):
        return self.stack.count == 0

    def size(self):
        return self.stack.count

    def pop(self):
        if self.size() != 0:
            item = self.stack[self.cursor]
            self.stack.delete(self.cursor)
            return item
        return None

    def push(self, value):
        self.stack.insert(self.cursor, value)

    def peek(self):
        if self.size() != 0:
            return self.stack[self.cursor]
        return None


class Queue:
    def __init__(self):
        self.main = Stack()
        self.swap = Stack()
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, item):
        self.main.push(item)
        self._size += 1

    def dequeue(self):
        if not self.isEmpty():
            if self.swap.isEmpty():
                while not self.main.isEmpty():
                    self.swap.push(self.main.pop())
            self._size -= 1
            return self.swap.pop()
        return None 

    def size(self):
        return self._size

    def rotate(self, n):
        if not self.isEmpty():
            for _ in range(n):
                self.enqueue(self.dequeue())
