import unittest

from stack import Stack

class TestStackMethods(unittest.TestCase):
    def test_stack_push(self):
        s = Stack()

        s.push(0)
        s.push(1)

        self.assertEqual(s.size(), 2)

    def test_stack_pop(self):
        s = Stack()

        s.push(0)
        s.push(1)

        i = s.pop()

        self.assertEqual(i, 1)
        self.assertEqual(s.size(), 1)

    def test_pop_from_empty_stack(self):
        s = Stack()

        i = s.pop()

        self.assertEqual(i, None)
        self.assertEqual(s.size(), 0)

    def test_stack_peek(self):
        s = Stack()

        s.push(0)
        s.push(1)

        i = s.peek()

        self.assertEqual(i, 1)
        self.assertEqual(s.size(), 2)

    def test_peek_from_empty_stack(self):
        s = Stack()

        i = s.peek()

        self.assertEqual(i, None)
        self.assertEqual(s.size(), 0)


if __name__ == '__main__':
    unittest.main()