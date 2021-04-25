class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key 
        self.NodeValue = val 
        self.Parent = parent 
        self.LeftChild = None 
        self.RightChild = None 

    def has_right_child(self):
        return self.RightChild is not None

    def has_left_child(self):
        return self.LeftChild is not None


class BSTFind: 
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False 
        self.ToLeft = False 
        

class BST:
    IN_ORDER = 0
    POST_ORDER = 1
    PRE_ORDER = 2

    def __init__(self, node):
        self.Root = node

    def isEmpty(self):
        return self.Root is None

    def FindNodeByKey(self, key):
        def find_in_subtree(node, key):
            if key == node.NodeKey:
                find_result = BSTFind()
                find_result.Node = node
                find_result.NodeHasKey = True
                return find_result
            elif key < node.NodeKey:
                if not node.has_left_child():
                    find_result = BSTFind()
                    find_result.Node = node
                    find_result.NodeHasKey = False
                    find_result.ToLeft = True
                    return find_result
                return find_in_subtree(node.LeftChild, key)
            else:
                if not node.has_right_child():
                    find_result = BSTFind()
                    find_result.Node = node
                    find_result.NodeHasKey = False
                    find_result.ToLeft = False
                    return find_result
                return find_in_subtree(node.RightChild, key)

        if self.isEmpty():
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
            while node.RightChild:
                node = node.RightChild
        else:
            while node.LeftChild:
                node = node.LeftChild
        return node
	
    def DeleteNodeByKey(self, key):
        find_result = self.FindNodeByKey(key)
        if not find_result.NodeHasKey:
            return False

        node_to_delete = find_result.Node

        delete_side = None if not node_to_delete.Parent else (True if node_to_delete.Parent.RightChild == node_to_delete else False)
        
        if node_to_delete.has_right_child():
            node_to_swap = self.FinMinMax(node_to_delete.RightChild, False)
        elif node_to_delete.has_left_child():
            node_to_swap = self.FinMinMax(node_to_delete.LeftChild, True)
        else:
            node_to_swap = None
        
        if node_to_swap is None:
            if delete_side is True:
                node_to_delete.Parent.RightChild = None
            elif delete_side is False:
                node_to_delete.Parent.LeftChild = None
            else:
                self.Root = None
            return True
        
        if node_to_swap.Parent.RightChild == node_to_swap:
            node_to_swap.Parent.RightChild = node_to_swap.LeftChild
            if node_to_swap.has_left_child():
                node_to_swap.LeftChild.Parent = node_to_swap.Parent
        else:
            node_to_swap.Parent.LeftChild = node_to_swap.RightChild
            if node_to_swap.has_right_child():
                node_to_swap.RightChild.Parent = node_to_swap.Parent
        
        if delete_side is True:
            node_to_delete.Parent.RightChild = node_to_swap
        elif delete_side is False:
            node_to_delete.Parent.LeftChild = node_to_swap
        else:
            self.Root = node_to_swap

        node_to_swap.Parent = node_to_delete.Parent
 
        node_to_swap.LeftChild = node_to_delete.LeftChild
        if node_to_swap.has_left_child():
            node_to_swap.LeftChild.Parent = node_to_swap
        
        node_to_swap.RightChild = node_to_delete.RightChild
        if node_to_swap.has_right_child():
            node_to_swap.RightChild.Parent = node_to_swap

        return True

    def Count(self):
        def count_subtree(node):
            result = 1
            if node.LeftChild is not None:
                result += count_subtree(node.LeftChild)
            if node.RightChild is not None:
                result += count_subtree(node.RightChild)
            return result

        if self.isEmpty():
            return 0

        return count_subtree(self.Root) 

    def WideAllNodes(self):
        if self.isEmpty():
            return tuple()

        result = []
        buffer = [self.Root]

        while len(buffer):
            node = buffer.pop(0)
            result.append(node)

            if node.LeftChild:
                buffer.append(node.LeftChild)
            if node.RightChild:
                buffer.append(node.RightChild)

        return tuple(result)

    def DeepAllNodes(self, method):
        def deep_nodes_in_order(node):
            result = []
            if node.LeftChild:
                result += deep_nodes_in_order(node.LeftChild)
            result.append(node)
            if node.RightChild:
                result += deep_nodes_in_order(node.RightChild)
            return result

        def deep_nodes_pre_order(node):
            result = []
            result.append(node)
            if node.LeftChild:
                result += deep_nodes_pre_order(node.LeftChild)
            if node.RightChild:
                result += deep_nodes_pre_order(node.RightChild)
            return result

        def deep_nodes_post_order(node):
            result = []
            if node.LeftChild:
                result += deep_nodes_post_order(node.LeftChild)
            if node.RightChild:
                result += deep_nodes_post_order(node.RightChild)
            result.append(node)
            return result

        if self.isEmpty():
            return tuple()

        if method == BST.IN_ORDER:
            result = deep_nodes_in_order(self.Root)
        elif method == BST.PRE_ORDER:
            result = deep_nodes_pre_order(self.Root)
        elif method == BST.POST_ORDER:
            result = deep_nodes_post_order(self.Root)
        else:
            raise ValueError('unexpected method')

        return tuple(result)





