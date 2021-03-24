import unittest

from set import PowerSet

class TestPowerSetMethods(unittest.TestCase):
    def test_put(self):
        s = PowerSet()

        s.put('One')
        self.assertEqual(s.get('One'), True)
        s.put('One')
        self.assertEqual(s.get('One'), True)

    def test_remove(self):
        s = PowerSet()

        s.put('One')

        self.assertEqual(s.get('One'), True)

        s.remove('One')

        self.assertEqual(s.get('One'), False)

    def test_intersection_empty(self):
        s = PowerSet()
        s2 = PowerSet()

        s.put('One')
        s.put('Two')
        s.put('Three')

        s2.put('Four')
        s2.put('Five')
        s2.put('Six')

        result = s.intersection(s2)

        self.assertEqual(result.size(), 0)

    def test_intersection_non_empty(self):
        s = PowerSet()
        s2 = PowerSet()

        s.put('One')
        s.put('Two')
        s.put('Three')

        s2.put('One')
        s2.put('Five')
        s2.put('Six')

        result = s.intersection(s2)

        self.assertEqual(result.size(), 1)

    def test_union(self):
        s = PowerSet()
        s2 = PowerSet()

        s.put('One')
        s.put('Two')
        s.put('Three')

        s2.put('Four')
        s2.put('Five')
        s2.put('Six')

        result = s.union(s2)

        self.assertEqual(result.size(), 6)

    def test_union_empty(self):
        s = PowerSet()
        s2 = PowerSet()

        result = s.union(s2)

        self.assertEqual(result.size(), 0)

    def test_difference(self):
        s = PowerSet()
        s2 = PowerSet()

        s.put('One')
        s.put('Two')
        s.put('Three')

        s2.put('One')
        s2.put('Two')
        s2.put('Six')

        result = s.difference(s2)

        self.assertEqual(result.size(), 1)

    def test_difference_empty(self):
        s = PowerSet()
        s2 = PowerSet()

        s.put('One')
        s.put('Two')
        s.put('Three')

        s2.put('One')
        s2.put('Two')
        s2.put('Three')

        result = s.difference(s2)

        self.assertEqual(result.size(), 0)

    def test_issubset(self):
        s = PowerSet()
        s2 = PowerSet()
        s3 = PowerSet()

        s.put('One')
        s.put('Two')
        s.put('Three')

        s2.put('One')
        s2.put('Two')

        s3.put('Four')
        s3.put('Five')

        self.assertEqual(s.issubset(s2), True)
        self.assertEqual(s.issubset(s3), False)


if __name__ == '__main__':
    unittest.main()
