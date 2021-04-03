class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key 
        self.NodeValue = val 
        self.Parent = parent 
        self.LeftChild = None 
        self.RightChild = None 


class BSTFind: 
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False 
        self.ToLeft = False 
        

class BST:
    def __init__(self, node):
        self.Root = node 

    def FindNodeByKey(self, key):
        def find_in_subtree(self, node, key):
            if key == node.NodeKey:
                find_result = BSTFind()
                find_result.Node = node
                find_result.NodeHasKey = True
                return find_result
            elif key < node.NodeKey:
                if node.LeftChild is None:
                    find_result = BSTFind()
                    find_result.Node = node
                    find_result.NodeHasKey = False
                    find_result.ToLeft = True
                    return find_result
                return find_in_subtree(node.LeftChild, key)
            else:
                if node.RightChild is None:
                    find_result = BSTFind()
                    find_result.Node = node
                    find_result.NodeHasKey = False
                    find_result.ToLeft = False
                    return find_result
                return find_in_subtree(node.RightChild, key)

        if self.Root is None:
            return BSTFind()

        return find_in_subtree(self.Root, key)

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)

        if find_result.NodeHasKey:
            return False

        new_node = BSTNode(key, val, find_result.Node)
        if find_result.Node is None:
            self.Root = new_node
        else:
            if find_result.ToLeft:
                find_result.Node.LeftChild = new_node
            else:
                find_result.Node.RightChild = new_node
        return True
  
    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if FindMax:
            while node.RightChild is not None:
                node = node.RightChild
        else:
            while node.LeftChild is not None:
                node = node.LeftChild
        return node
	
    def DeleteNodeByKey(self, key):
        find_result = self.FindNodeByKey(key)
        if not find_result.NodeHasKey:
            return False

        delete = find_result.Node

        SIDE_LEFT = 'left'
        SIDE_RIGHT = 'right'
        SIDE_NONE = 'none'
        if delete.Parent:
            delete_side = SIDE_RIGHT if delete.Parent.RightChild == delete else SIDE_LEFT
        else:
            delete_side = SIDE_NONE
        
        if delete.RightChild is not None:
            swap = self.FinMinMax(delete.RightChild, False)
        elif delete.LeftChild is not None:
            swap = self.FinMinMax(delete.LeftChild, True)
        else:
            swap = None
        
        if swap is None:
            if delete_side == SIDE_RIGHT:
                delete.Parent.RightChild = None
            elif delete_side == SIDE_LEFT:
                delete.Parent.LeftChild = None
            else:
                self.Root = None
            return True
        
        swap_right = swap.Parent.RightChild == swap
        
        if swap_right:
            swap.Parent.RightChild = swap.LeftChild
            if swap.LeftChild is not None:
                swap.LeftChild.Parent = swap.Parent
        else:
            swap.Parent.LeftChild = swap.RightChild
            if swap.RightChild is not None:
                swap.RightChild.Parent = swap.Parent
        
        if delete_side == SIDE_RIGHT:
            delete.Parent.RightChild = swap
        elif delete_side == SIDE_LEFT:
            delete.Parent.LeftChild = swap
        else:
            self.Root = swap

        swap.Parent = delete.Parent
 
        swap.LeftChild = delete.LeftChild
        if swap.LeftChild is not None:
            swap.LeftChild.Parent = swap
        
        swap.RightChild = delete.RightChild
        if swap.RightChild is not None:
            swap.RightChild.Parent = swap

        return True

    def Count(self):
        def count_subtree(node):
            result = 1
            if node.LeftChild is not None:
                result += self.count_subtree(node.LeftChild)
            if node.RightChild is not None:
                result += self.count_subtree(node.RightChild)
            return result

        if self.Root is None:
            return 0

        return count_subtree(self.Root) 


