import unittest

from solve import count_nice_one, count_nice_two


class MyTestCase(unittest.TestCase):
    def test_count_nice_one(self):
        self.assertEqual(count_nice_one(["ugknbfddgicrmopn"]), 1)
        self.assertEqual(count_nice_one(["aaa"]), 1)
        self.assertEqual(count_nice_one(["jchzalrnumimnmhp"]), 0)
        self.assertEqual(count_nice_one(["haegwjzuvuyypxyu"]), 0)
        self.assertEqual(count_nice_one(["dvszwmarrgswjxmb"]), 0)

    def test_count_nice_two(self):
        self.assertEqual(count_nice_two(["qjhvhtzxzqqjkmpb"]), 1)
        self.assertEqual(count_nice_two(["xxyxx"]), 1)
        self.assertEqual(count_nice_two(["uurcxstgmygtbstg"]), 0)
        self.assertEqual(count_nice_two(["ieodomkazucvgmuy"]), 0)


if __name__ == '__main__':
    unittest.main()
