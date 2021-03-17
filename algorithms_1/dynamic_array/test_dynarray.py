import unittest

from dynarray import DynArray

class TestDynArrayMethods(unittest.TestCase):
    def test_insert_without_overflow(self):
        d = DynArray()
        count = 10

        for i in range(0, count):
            d.append(i)

        d.insert(8, 10)

        self.assertEqual(d.count, count + 1)
        self.assertEqual(d.capacity, 16)

    def test_insert_with_overflow(self):
        d = DynArray()
        count = 16
        capacity = d.capacity

        for i in range(0, count):
            d.append(i)

        d.insert(16, 17)

        self.assertEqual(d.count, count + 1)
        self.assertEqual(d.capacity, capacity * 2)

    def test_insert_with_overflow_2(self):
        d = DynArray()
        count = 16
        capacity = d.capacity

        for i in range(0, count):
            d.append(i)

        self.assertEqual(d.count, count)
        self.assertEqual(d.capacity, capacity)

        d.insert(17, 17)

        self.assertEqual(d.count, count + 1)
        self.assertEqual(d.capacity, capacity*2)

    def test_insert_out_of_bound(self):
        d = DynArray()

        for i in range(0, 10):
            d.append(i)

        with self.assertRaises(IndexError):
            d.insert(11, 10)

    def test_delete_without_resizing(self):
        d = DynArray()
        count = 8
        capacity = d.capacity

        for i in range(0, count):
            d.append(i)

        d.delete(3)

        self.assertEqual(d.count, count - 1)
        self.assertEqual(d.capacity, capacity)

    def test_delete_without_resizing(self):
        d = DynArray()
        count = 20
        capacity = d.capacity

        for i in range(0, count):
            d.append(i)

        self.assertEqual(d.count, count)
        self.assertEqual(d.capacity, capacity * 2)

        for i in range(0, 5):
            d.delete(i)

        self.assertEqual(d.capacity, 21)

        for i in range(0, 5):
            d.delete(i)

        self.assertEqual(d.count, count / 2)
        self.assertEqual(d.capacity, 16)

    def test_insert_out_of_bound(self):
        d = DynArray()
        count =  10

        for i in range(0, count):
            d.append(i)

        with self.assertRaises(IndexError):
            d.delete(-1)

        with self.assertRaises(IndexError):
            d.delete(count + 1)



if __name__ == '__main__':
    unittest.main()