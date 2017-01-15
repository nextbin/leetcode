import unittest

from solution.ac3 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring('ggububgvfk'), 6)
        self.assertEqual(solution.lengthOfLongestSubstring('nfpdmpi'), 5)
        self.assertEqual(solution.lengthOfLongestSubstring('dvdf'), 3)
        self.assertEqual(solution.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(solution.lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(solution.lengthOfLongestSubstring('pwwkew'), 3)
        self.assertEqual(solution.lengthOfLongestSubstring('a'), 1)
        self.assertEqual(solution.lengthOfLongestSubstring(None), 0)
        self.assertEqual(solution.lengthOfLongestSubstring(''), 0)


if __name__ == '__main__':
    unittest.main()
