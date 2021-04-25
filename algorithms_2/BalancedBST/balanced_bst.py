class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key 
        self.Parent = parent 
        self.LeftChild = None 
        self.RightChild = None 
        self.Level = 0 

    def add_childs(self, left=None, right=None):
        self.LeftChild = left
        self.RightChild = right

    
    def count_subnodes(self):
        subnodes_counter = 1
        if self.LeftChild is not None:
            subnodes_counter += self.LeftChild.count_subnodes()
        if self.RightChild is not None:
            subnodes_counter += self.RightChild.count_subnodes()

        return subnodes_counter

    def is_subtree_balanced(self):
        left_side_subnodes_counter = self.LeftChild.count_subnodes() if self.LeftChild else 0
        right_side_subnodes_counter = self.RightChild.count_subnodes() if self.RightChild else 0

        if (
            abs(left_side_subnodes_counter - right_side_subnodes_counter) > 1 or
            self.LeftChild and not self.LeftChild.is_subtree_balanced() or
            self.RightChild and not self.RightChild.is_subtree_balanced()
        ):
            return False

        return True

        
class BalancedBST:

    def __init__(self):
        self.Root = None 

    def GenerateTree(self, a):
        def fill_tree(parent_node, a):
            if not a:
                return

            level = parent_node.Level + 1 if parent_node else 1
            middle = len(a) // 2
            node = BSTNode(a[middle], parent_node)
            node.Level = level
            node.LeftChild = fill_tree(node, a[:middle])
            node.RightChild = fill_tree(node, a[middle+1:])

            return node

        if not a:
            return []

        self.Root = fill_tree(None, sorted(a))

    def IsBalanced(self, root_node):
        return root_node.is_subtree_balanced()
