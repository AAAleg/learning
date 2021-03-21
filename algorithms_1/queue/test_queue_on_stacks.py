import unittest

from queue import Queue

class TestDynArrayMethods(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.size(), 3)
        self.assertEqual(q.items, [3,2,1])

    def test_qequeue(self):
        q = Queue()
        items = [1,2,3,4]
        [q.enqueue(i) for i in items]

        self.assertEqual(q.size(), len(items))

        result = []
        while not q.isEmpty():
            result.append(q.dequeue())

        self.assertEqual(result, items)

    def test_dequeue_from_empty_queue(self):
        q = Queue()

        self.assertEqual(q.size(), 0)
        self.assertEqual(q.dequeue(), None)

    def test_rotate(self):
        q = Queue()
        items = [1,2,3,4,5]
        expected = [3,4,5,1,2]
        [q.enqueue(i) for i in items]

        q.rotate(2)

        result = []
        while not q.isEmpty():
            result.append(q.dequeue())

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()