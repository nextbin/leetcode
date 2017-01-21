import unittest

from ac11 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        self.assertEqual(solution.maxArea(None), 0)
        self.assertEqual(solution.maxArea([1, 1]), 1)
        self.assertEqual(solution.maxArea([1, 2, 3, 4]), 4)
        self.assertEqual(solution.maxArea([4, 2, 3, 4]), 12)


if __name__ == '__main__':
    unittest.main()
