import unittest

from ordered_list import OrderedList


class TestOrderedListMethods(unittest.TestCase):
	
	def test_add_ascending(self):
		ol = OrderedList(asc=True)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)
		items.sort()
		self.assertEqual([node.value for node in ol.get_all()], items)

	def test_add_descending(self):
		ol = OrderedList(asc=False)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)

		items.sort(reverse=True)
		self.assertEqual([node.value for node in ol.get_all()], items)

	def test_delete_ascending(self):
		ol = OrderedList(asc=True)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)

		items.sort()
		items.remove(5)

		ol.delete(5)

		self.assertEqual([node.value for node in ol.get_all()], items)

	def test_delete_ascending_begin(self):
		ol = OrderedList(asc=True)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)

		items.sort()
		items.remove(2)

		ol.delete(2)

		self.assertEqual([node.value for node in ol.get_all()], items)

	def test_delete_ascending_end(self):
		ol = OrderedList(asc=True)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)

		items.sort()
		items.remove(8)

		ol.delete(8)

		self.assertEqual([node.value for node in ol.get_all()], items)

	def test_delete_descending(self):
		ol = OrderedList(asc=False)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)

		items.sort(reverse=True)
		items.remove(5)

		ol.delete(5)

		self.assertEqual([node.value for node in ol.get_all()], items)

	def test_delete_descending_begin(self):
		ol = OrderedList(asc=False)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)

		items.sort(reverse=True)
		items.remove(2)

		ol.delete(2)

		self.assertEqual([node.value for node in ol.get_all()], items)

	def test_delete_descending_end(self):
		ol = OrderedList(asc=False)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)

		items.sort(reverse=True)
		items.remove(8)

		ol.delete(8)

		self.assertEqual([node.value for node in ol.get_all()], items)

	def test_find_by_value_ascending(self):
		ol = OrderedList(asc=True)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)

		node = ol.find(2)

		self.assertEqual(node.value, 2)

	def test_find_by_value_descending(self):
		ol = OrderedList(asc=True)

		items = [4,6,2,8,5]

		for item in items:
			ol.add(item)

		node = ol.find(4)

		self.assertEqual(node.value, 4)


if __name__ == '__main__':
	unittest.main()
