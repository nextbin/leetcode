import unittest

from ac15 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
        print(solution.threeSum([0, 0, 0]))
        print(solution.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))


if __name__ == '__main__':
    unittest.main()
