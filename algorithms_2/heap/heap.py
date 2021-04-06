class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * self.calculate_length(depth)  
        for key in a:
            self.Add(key)
        
    def GetMax(self):
        if self.isEmpty():
            return -1

        result = self.HeapArray[0]
        index = self.last_index()
        self.HeapArray[0] = self.HeapArray[index]
        self.HeapArray[index] = None
        self.sift_down(0)

        return result

    def Add(self, key):
        index = self.free_index()

        if index is None:
            return False

        self.HeapArray[index] = key
        self.sift_up(index)
        return True

    def sift_down(self, index):
        left_child = self.get_left_child(index)
        right_child = self.get_right_child(index)

        if not self.exists(left_child) and not self.exists(right_child):
            return 
        elif not self.exists(left_child):
            max_item = right_child
        elif not self.exists(right_child):
            max_item = left_child
        else:
            max_item = max(left_child, right_child, key=lambda i: self.HeapArray[i])

        if self.HeapArray[max_item] > self.HeapArray[index]:
            self.HeapArray[max_item], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[max_item]
            self.sift_down(max_item)

    def sift_up(self, index):
        parent = self.get_parent(index)

        if not self.check_boundaries(parent):
            return

        if self.HeapArray[parent] < self.HeapArray[index]:
            self.HeapArray[parent], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[parent]
            self.sift_up(parent)
    
    @staticmethod
    def calculate_length(depth):
        return 2 ** (depth - 1) + 1

    def free_index(self):
        for i, key in enumerate(self.HeapArray):
            if key is None:
                return i
        return None

    def last_index(self):
        index = self.free_index()
        if index is None:
            return len(self.HeapArray) - 1
        elif index == 0:
            return None
        else:
            return index - 1


    def isEmpty(self):
        return len(self.HeapArray) == 0 or self.HeapArray[0] is None

    @staticmethod
    def calculate_length(depth):
        return 2 ** (depth + 1) - 1

    @staticmethod
    def get_left_child(index):
        return 2 * index + 1

    @staticmethod
    def get_right_child(index):
        return 2 * index + 2

    @staticmethod
    def get_parent(index):
        return (index - 1) // 2

    def exists(self, index):
        return self.check_boundaries(index) and self.HeapArray[index] is not None

    def check_boundaries(self, index):
        return 0 <= index < len(self.HeapArray)
