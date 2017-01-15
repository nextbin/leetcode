import unittest
from solution.ac65 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        self.assertEqual(solution.isNumber(' 005e+6'), True)
        self.assertEqual(solution.isNumber('.2e81'), True)
        self.assertEqual(solution.isNumber('.2e'), False)
        self.assertEqual(solution.isNumber('.e1'), False)
        self.assertEqual(solution.isNumber('3.09e'), False)
        self.assertEqual(solution.isNumber('6e6.5'), False)
        self.assertEqual(solution.isNumber('+46.e3'), True)
        self.assertEqual(solution.isNumber('+.9'), True)
        self.assertEqual(solution.isNumber('-7e'), False)
        self.assertEqual(solution.isNumber('-7e1'), True)
        self.assertEqual(solution.isNumber('-.1'), True)
        self.assertEqual(solution.isNumber('-1'), True)
        self.assertEqual(solution.isNumber('-1.'), True)
        self.assertEqual(solution.isNumber('-1.1'), True)
        self.assertEqual(solution.isNumber('3.'), True)
        self.assertEqual(solution.isNumber('.1'), True)
        self.assertEqual(solution.isNumber(''), False)
        self.assertEqual(solution.isNumber(' '), False)
        self.assertEqual(solution.isNumber(None), False)
        self.assertEqual(solution.isNumber('0'), True)
        self.assertEqual(solution.isNumber('00'), True)
        self.assertEqual(solution.isNumber(' 0.1 '), True)
        self.assertEqual(solution.isNumber(' abc '), False)
        self.assertEqual(solution.isNumber('1 a'), False)
        self.assertEqual(solution.isNumber('2e10'), True)
        self.assertEqual(solution.isNumber('2e'), False)
        self.assertEqual(solution.isNumber('e'), False)
        self.assertEqual(solution.isNumber('.'), False)


if __name__ == '__main__':
    unittest.main()
