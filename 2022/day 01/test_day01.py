import unittest

from solve import calories_top_elves

elves = ["1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"]

class MyTestCase(unittest.TestCase):
    def test_calories_top_elves(self):
        self.assertEqual(calories_top_elves(elves, 1), 24000)
        self.assertEqual(calories_top_elves(elves, 3), 45000)


if __name__ == '__main__':
    unittest.main()