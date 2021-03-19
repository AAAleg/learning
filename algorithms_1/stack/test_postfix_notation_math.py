import unittest

from postfix_notation_math import calculate

class TestPostfixNotation(unittest.TestCase):
    def test_postfix_notation(self):
    	expression = '8 2 + 5 * 9 + ='

    	result = calculate(expression)

    	self.assertEqual(result, 59)


if __name__ == '__main__':
    unittest.main()