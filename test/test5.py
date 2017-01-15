import unittest

from solution.ac5 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        self.assertEqual(solution.longestPalindrome('a'), 'a')
        self.assertEqual(solution.longestPalindrome('ccd'), 'cc')
        self.assertEqual(solution.longestPalindrome(''), '')
        self.assertRegex(solution.longestPalindrome('babad'), 'bab|aba')
        self.assertEqual(solution.longestPalindrome('cbbd'), 'bb')


if __name__ == '__main__':
    unittest.main()
