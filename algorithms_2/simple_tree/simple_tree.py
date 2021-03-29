class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root
	
    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
  
    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.parent = None

    def GetAllNodes(self):
        def walk(node):
            result = [node]
            for child in node.Children:
                result += walk(child)
            return result

        if self.Root is None:
            return []

        return walk(self.Root)

    def FindNodesByValue(self, val):
        def walk(node, val):
            result = []
            if node.NodeValue == val:
                result.append(node)
            for child in node.Children:
                result += walk(child, val)
            return result

        if self.Root is None:
            return []

        return walk(self.Root, val)
   
    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode.parent is not self.Root:    
            self.DeleteNode(OriginalNode)
            self.AddChild(NewParent, OriginalNode)
   
    def Count(self):
        def count_node_subtree(node):
            return 1 + sum(count_node_subtree(child) for child in node.Children)

        if self.Root is None:
            return 0

        return count_node_subtree(self.Root)

    def LeafCount(self):
        def leaf_count_subtree(node):
            if not node.Children:
                return 1

            return sum(leaf_count_subtree(child) for child in node.Children)

        if self.Root is None:
            return 0

        return leaf_count_subtree(self.Root)
