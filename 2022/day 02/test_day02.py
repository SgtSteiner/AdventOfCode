import unittest

from solve import calc_score_round_part_one, calc_score_round_part_two

data = [["A", "Y"], ["B", "X"], ["C", "Z"]]

class MyTestCase(unittest.TestCase):
    def test_calc_score_round_part_one(self):
        self.assertEqual(calc_score_round_part_one(data), 15)
        
    def test_calc_score_round_part_two(self):
        self.assertEqual(calc_score_round_part_two(data), 12)

if __name__ == '__main__':
    unittest.main()