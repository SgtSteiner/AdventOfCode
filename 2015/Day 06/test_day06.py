import unittest

from solve import action_lights, action_brightness


class MyTestCase(unittest.TestCase):
    def test_action_lights(self):
        self.assertEqual(action_lights(["turn on 0,0 through 999,999"]), 1000000)
        self.assertEqual(action_lights(["turn on 0,0 through 999,0"]), 1000)
        self.assertEqual(action_lights(["turn on 0,0 through 999,999",
                                        "toggle 0,0 through 999,0"]), 999000)
        self.assertEqual(action_lights(["turn off 499,499 through 500,500"]), 0)
        self.assertEqual(action_lights(["turn on 0,0 through 999,999",
                                        "turn off 499,499 through 500,500"]), 999996)

    def test_action_brightness(self):
        self.assertEqual(action_brightness(["turn on 0,0 through 999,999",
                                            "turn on 0,0 through 0,999",
                                            "turn on 0,0 through 999,0"]), 1002000)


if __name__ == '__main__':
    unittest.main()
