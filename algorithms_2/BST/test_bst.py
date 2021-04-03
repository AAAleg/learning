import unittest

from bst import BST, BSTNode

class TestBSTMethods(unittest.TestCase):
	def test_delete(self):
		root = BSTNode(10, 10, None)
		tree = BST(root)
		tree.DeleteNodeByKey(10)
		

if __name__ == '__name__':
	unittest.main()
