import unittest

from solve import action_grid


class MyTestCase(unittest.TestCase):
    def test_action_lights(self):
        self.assertEqual(action_grid(["turn on 0,0 through 999,999"], "lights"), 1000000)
        self.assertEqual(action_grid(["turn on 0,0 through 999,0"], "lights"), 1000)
        self.assertEqual(action_grid(["turn on 0,0 through 999,999",
                                      "toggle 0,0 through 999,0"], "lights"), 999000)
        self.assertEqual(action_grid(["turn off 499,499 through 500,500"], "lights"), 0)
        self.assertEqual(action_grid(["turn on 0,0 through 999,999",
                                      "turn off 499,499 through 500,500"], "lights"), 999996)

    def test_action_brightness(self):
        self.assertEqual(action_grid(["turn on 0,0 through 999,999",
                                      "turn on 0,0 through 0,999",
                                      "turn on 0,0 through 999,0"], "brightness"), 1002000)


if __name__ == '__main__':
    unittest.main()
