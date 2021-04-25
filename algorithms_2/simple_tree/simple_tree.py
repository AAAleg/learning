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
            all_nodes = [node]
            for child in node.Children:
                all_nodes += walk(child)
            return all_nodes

        if self.Root is None:
            return []

        return walk(self.Root)

    def FindNodesByValue(self, val):
        def walk(node, val):
            founded_elements = []
            if node.NodeValue == val:
                founded_elements.append(node)
            for child in node.Children:
                founded_elements += walk(child, val)
            return founded_elements

        if self.Root is None:
            return []

        return walk(self.Root, val)
   
    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode is not self.Root:    
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

    def EvenTrees(self):
        even_trees = []

        for child in self.Root.Children:
            subtree = SimpleTree(child)
            if subtree.Count() % 2 == 0:
                even_trees += [self.Root, child]
            even_trees += subtree.EvenTrees()

        return even_trees
