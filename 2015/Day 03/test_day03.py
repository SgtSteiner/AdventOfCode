import unittest

from solve import house_santa, house_robosanta


class MyTestCase(unittest.TestCase):
    def test_house_santa(self):
        self.assertEqual(house_santa(list(">")), 2)
        self.assertEqual(house_santa(list("^>v<")), 4)
        self.assertEqual(house_santa(list("^v^v^v^v^v")), 2)

    def test_house_robosanta(self):
        self.assertEqual(house_robosanta(list("^v")), 3)
        self.assertEqual(house_robosanta(list("^>v<")), 3)
        self.assertEqual(house_robosanta(list("^v^v^v^v^v")), 11)


if __name__ == '__main__':
    unittest.main()
