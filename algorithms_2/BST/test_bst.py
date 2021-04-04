import unittest

from bst import BST, BSTNode

class TestBSTMethods(unittest.TestCase):
	def test_delete_root(self):
		root = BSTNode(10, 10, None)
		tree = BST(root)
		tree.DeleteNodeByKey(10)

		self.assertEqual(tree.Count(), 0)

	def test_count_root(self):
		root = BSTNode(10, 10, None)
		tree = BST(root)
		node = BSTNode(15, 10, None)
		tree.AddKeyValue(15,10)

		self.assertEqual(tree.Count(), 2)

if __name__ == '__name__':
	unittest.main()
