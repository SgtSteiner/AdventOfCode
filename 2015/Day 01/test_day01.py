import unittest

from solve import calc_floor, call_basement


class MyTestCase(unittest.TestCase):
    def test_floor(self):
        self.assertEqual(calc_floor(list("(())")), 0)
        self.assertEqual(calc_floor(list("()()")), 0)
        self.assertEqual(calc_floor(list("(((")), 3)
        self.assertEqual(calc_floor(list("(()(()(")), 3)
        self.assertEqual(calc_floor(list("))(((((")), 3)
        self.assertEqual(calc_floor(list("())")), -1)
        self.assertEqual(calc_floor(list("))(")), -1)
        self.assertEqual(calc_floor(list(")))")), -3)
        self.assertEqual(calc_floor(list(")())())")), -3)

    def test_basement(self):
        self.assertEqual(call_basement(list(")")), 1)
        self.assertEqual(call_basement(list("()())")), 5)


if __name__ == '__main__':
    unittest.main()
