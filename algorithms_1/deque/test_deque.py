import unittest

from deque import Deque

class TestDequeueMethods(unittest.TestCase):
    def test_add_front(self):
        d = Deque()
        items = [1,2,3,4,5]

        [d.addFront(i) for i in items]

        self.assertEqual(d.size(), len(items))
        self.assertEqual(d.items, items)

    def test_add_tail(self):
        d = Deque()
        items = [1,2,3,4,5]

        [d.addTail(i) for i in items]

        self.assertEqual(d.size(), len(items))
        self.assertEqual(d.items, items[::-1])

    def test_remove_front(self):
        d = Deque()
        items = [1,2,3,4,5]

        [d.addFront(i) for i in items]

        self.assertEqual(d.size(), len(items))
        self.assertEqual(d.items, items)

        d.removeFront()

        self.assertEqual(d.size(), len(items) - 1)
        self.assertEqual(d.items, items[:-1])

    def test_remove_tail(self):
        d = Deque()
        items = [1,2,3,4,5]

        [d.addTail(i) for i in items]

        self.assertEqual(d.size(), len(items))
        self.assertEqual(d.items, items[::-1])

        d.removeTail()

        self.assertEqual(d.size(), len(items) - 1)
        self.assertEqual(d.items, items[::-1][1:])
        
if __name__ == '__main__':
    unittest.main()