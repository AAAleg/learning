import unittest

from parentheses_balance import parentheses_balance

class TestParenthesesBalance(unittest.TestCase):
    def test_parentheses_balanced(self):
    	strings = ['((()))', '(()()())', '()()((()))', '()()()']
    	for string in strings:
    		self.assertEqual(parentheses_balance(string), True)

    def test_parentheses_not_balanced(self):
    	strings = ['(()', '())(', '))((', '((())']
    	for string in strings:
    		self.assertEqual(parentheses_balance(string), False)


if __name__ == '__main__':
    unittest.main()