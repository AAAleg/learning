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
            return index
        self.Tree[-index] = key
        return -index

    def isEmpty(self):
        return self.Tree[0] is None

    def getLeftChildIndex(self, index):
        return index * 2 + 1

    def getRightChildIndex(self, index):
        return index * 2 + 2


def GenerateBBSTArray(array):
    if not array:
        return []

    sorted_array = sorted(array)
    depth = calculate_depth(len(sorted_array))
    result = [None] * calculate_length(depth)
    fill_tree(sorted_array, 0, result)

    return result


def calculate_length(depth):
    return 2 ** (depth + 1) - 1


def calculate_depth(count):
    depth = 0
    while calculate_length(depth) < count:
        depth += 1
    return depth


def fill_tree(array, index, tree):
    if not array:
        return

    middle = len(array) // 2
    tree[index] = array[middle]

    fill_tree(array[:middle], index * 2 + 1, tree)
    fill_tree(array[middle+1:], index * 2 + 2, tree)
