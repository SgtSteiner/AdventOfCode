import unittest

from solve import feet_paper, feet_ribbon


class MyTestCase(unittest.TestCase):
    def test_feet_paper(self):
        self.assertEqual(feet_paper(["2x3x4"]), 58)
        self.assertEqual(feet_paper(["1x1x10"]), 43)

    def test_feet_ribbon(self):
        self.assertEqual(feet_ribbon(["2x3x4"]), 34)
        self.assertEqual(feet_ribbon(["1x1x10"]), 14)


if __name__ == '__main__':
    unittest.main()
