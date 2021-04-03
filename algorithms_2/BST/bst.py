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
        cursor = BSTFind()
        cursor.Node = self.Root
        while cursor.Node.NodeKey != key:
            if key >= node.Node.NodeKey:
                if cursor.Node.RightChild is None:
                    break
                cursor.Node = cursor.Node.RightChild
            else:
                if cursor.Node.LeftChild is None:
                    cursor.ToLeft = True
                    break
                cursor.Node = cursor.Node.LeftChild
        else:
            cursor.NodeHasKey = True

        return cursor 

    def AddKeyValue(self, key, val):
        cursor = self.FindNodeByKey(key)
        node = BSTNode(key, val, None)
        if cursor.NodeHasKey is False:
            if cursor.ToLeft is False:
                node.Node.RightChild = node
            else:
                node.Node.LeftChild = node
            node.Parent = cursor.Node
            return True
        else:
            return False 
  
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
            if node.LeftChild is not None:
                return 1 + sum(count_subtree(node.LeftChild))
            if node.RightChild is not None:
                return 1 + sum(count_subtree(node.RightChild))

        if self.Root is None:
            return 0

        return count_subtree(self.Root) 


