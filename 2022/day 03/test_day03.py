import unittest

from solve import calc_item_type, calc_item_type_badge

data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

class MyTestCase(unittest.TestCase):
    def test_calc_item_type(self):
        self.assertEqual(calc_item_type(data), 157)
        
    def test_calc_item_type_badge(self):
        self.assertEqual(calc_item_type_badge(data), 70)

if __name__ == '__main__':
    unittest.main()