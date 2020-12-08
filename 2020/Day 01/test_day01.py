import unittest

from solve import suma_tupla


class MyTestCase(unittest.TestCase):
    def test_suma_tupla(self):
        self.assertEqual(suma_tupla([1721, 979, 366, 299, 675, 1456], 2), 514579)
        self.assertEqual(suma_tupla([1721, 979, 366, 299, 675, 1456], 3), 241861950)


if __name__ == '__main__':
    unittest.main()
