class aBST:

    def __init__(self, depth):
        tree_size = sum(2 ** n for n in range(depth + 1))
        self.Tree = [None] * tree_size
	
    def FindKeyIndex(self, key):
        index = 0

        while index < len(self.Tree):
            if self.Tree[index] is None:
                return -index
            elif self.Tree[index] == key:
                return index
            elif self.Tree[index] > key:
                index = self.getLeftChildIndex(index)
            else:
                index = self.getRightChildIndex(index)

        return None
	
    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index > 0:
            return 0
        self.Tree[-index] = key
        return -index

    def isEmpty(self):
        return self.Tree[0] is None

    def getLeftChildIndex(index):
        return index * 2 + 1

    def getRightChildIndex(index):
        return index * 2 + 2