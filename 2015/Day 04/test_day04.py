import unittest

from solve import get_md5hash


class MyTestCase(unittest.TestCase):
    def test_get_md5hash(self):
        self.assertEqual(get_md5hash("abcdef", 5), 609043)
        self.assertEqual(get_md5hash("pqrstuv", 5), 1048970)


if __name__ == '__main__':
    unittest.main()
