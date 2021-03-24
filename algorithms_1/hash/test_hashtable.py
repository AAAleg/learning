import unittest

from hashtable import HashTable


class TestHashMethods(unittest.TestCase):
	
	def test_hash_fun(self):
		size = 115
		step = 30
		h = HashTable(size, step)
		
		self.assertEqual(h.hash_fun("python"), 99)

	def test_seek_slot(self):
		size = 38
		step = 5
		h = HashTable(size, step)

		for i in range(size):
			h.slots[h.seek_slot("python")] = "python"
		for i in range(size):
			self.assertEqual(h.slots[i], "python")

		self.assertEqual(h.seek_slot("python"), None)

	def test_put(self):
		size = 8
		step = 2
		h = HashTable(size, step)

		for i in range(size):
			h.put("python")
		for i in range(size):
			self.assertEqual(h.slots[i], "python")

		self.assertEqual(h.seek_slot("python"), None)

	def test_find(self):
		size = 30
		step = 2
		h = HashTable(size, step)

		h.put("One")
		h.put("Two")
		h.put("Three")

		self.assertEqual(h.find("One"), h.hash_fun("One"))
		self.assertEqual(h.find("Two"), h.hash_fun("Two"))
		self.assertEqual(h.find("Three"), h.hash_fun("Three"))
		self.assertEqual(h.find("Four"), None)



if __name__ == '__main__':
	unittest.main()
