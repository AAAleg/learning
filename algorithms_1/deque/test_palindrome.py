import unittest

from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        strings = {
            'dovod': True,
            'nedovod': False,
            'parrap': True,
            'neparrap': False
        }

        for string, prediction in strings.items():
            self.assertEqual(is_palindrome(string), prediction)

        
if __name__ == '__main__':
    unittest.main()