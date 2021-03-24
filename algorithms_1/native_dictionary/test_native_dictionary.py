import unittest

from native_dictionary import NativeDictionary


class TestNativeDictionaryMethods(unittest.TestCase):
	
	def test_get(self):
		d = NativeDictionary(5)

		self.assertEqual(d.get('zero'), None)

		d.put('one', 1)

		self.assertEqual(d.get('one'), 1)
		self.assertEqual(d.get('two'), None)

	def test_put(self):
		d = NativeDictionary(5)

		d.put('one', 1)

		self.assertEqual(d.get('one'), 1)

		d.put('one', 2)

		self.assertEqual(d.get('one'), 2)

	def test_is_key(self):
		d = NativeDictionary(5)

		self.assertEqual(d.is_key('one'), False)

		d.put('one', 1)

		self.assertEqual(d.is_key('one'), True)
		self.assertEqual(d.is_key('two'), False)



if __name__ == '__main__':
	unittest.main()
