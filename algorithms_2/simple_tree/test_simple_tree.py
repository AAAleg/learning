import unittest

from simple_tree import SimpleTree, SimpleTreeNode


class TestSimpleTreeMethods(unittest.TestCase):
    def test_add_child(self):
        root = SimpleTreeNode(0, None)
        tree = SimpleTree(root)
        node = SimpleTreeNode(1, None)

        tree.AddChild(root, node)

        self.assertEqual(root.Children, [node])
        self.assertEqual(node.Parent, root)

    def test_delete_child(self):
        pass

    def test_get_all_nodes_empty_tree(self):
        tree = SimpleTree(None)

        self.assertEqual(tree.GetAllNodes(), [])

    def test_get_all_nodes(self):
        root = SimpleTreeNode(0, None)
        tree = SimpleTree(root)

        node = SimpleTreeNode(1, None)
        node2 = SimpleTreeNode(2, None)

        expected_nodes = [root, node, node2]


        tree.AddChild(root, node)
        tree.AddChild(root, node2)

        nodes = tree.GetAllNodes()

        self.assertEqual(len(nodes), len(expected_nodes))
        for item in expected_nodes:
            self.assertIn(item, nodes)

    def test_find_nodes_by_value(self):
        root = SimpleTreeNode(0, None)
        tree = SimpleTree(root)

        node = SimpleTreeNode(1, None)
        node2 = SimpleTreeNode(2, None)
        node3 = SimpleTreeNode(3, None)
        node4 = SimpleTreeNode(1, None)
        node5 = SimpleTreeNode(5, None)
        node6 = SimpleTreeNode(1, None)


        expected_nodes = [node, node4, node6]


        tree.AddChild(root, node)
        tree.AddChild(root, node2)
        tree.AddChild(root, node3)
        tree.AddChild(node3, node4)
        tree.AddChild(node3, node5)
        tree.AddChild(node3, node6)

        nodes = tree.FindNodesByValue(1)

        self.assertEqual(len(nodes), len(expected_nodes))
        for item in expected_nodes:
            self.assertIn(item, nodes)


    def test_count_nodes(self):
        root = SimpleTreeNode(0, None)
        tree = SimpleTree(root)

        node = SimpleTreeNode(1, None)
        node2 = SimpleTreeNode(2, None)
        node3 = SimpleTreeNode(3, None)
        node4 = SimpleTreeNode(1, None)
        node5 = SimpleTreeNode(5, None)
        node6 = SimpleTreeNode(1, None)

        tree.AddChild(root, node)
        tree.AddChild(root, node2)
        tree.AddChild(root, node3)
        tree.AddChild(node3, node4)
        tree.AddChild(node3, node5)
        tree.AddChild(node3, node6)

        self.assertEqual(tree.Count(), 7)

    def test_count_leaf(self):
        root = SimpleTreeNode(0, None)
        tree = SimpleTree(root)

        node = SimpleTreeNode(1, None)
        node2 = SimpleTreeNode(2, None)
        node3 = SimpleTreeNode(3, None)
        node4 = SimpleTreeNode(1, None)
        node5 = SimpleTreeNode(5, None)
        node6 = SimpleTreeNode(1, None)

        tree.AddChild(root, node)
        tree.AddChild(root, node2)
        tree.AddChild(root, node3)
        tree.AddChild(node3, node4)
        tree.AddChild(node3, node5)
        tree.AddChild(node3, node6)

        self.assertEqual(tree.LeafCount(), 5)


if __name__ == '__main__':
    unittest.main()
