import unittest

from cache import NativeCache

class TestNativeCacheMethods(unittest.TestCase):
	def test_put(self):
		cache = NativeCache(5)
		items = {
			'one': 'I',
			'two': 'II',
			'three': 'III',
			'four': '4',
			'five': 'V'
		}

		for key, value in items.items():
			cache.put(key, value)
		items_list = list(items.items())
		item = items_list.pop()

		for itm in items_list:
			for _ in range(3):
				cache.get(itm)

		cache.put('six', 'VI')

		self.assertEqual(cache.is_key(item), False)


if __name__ == '__main__':
	unittest.main()
