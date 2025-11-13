import unittest
import test


class TestCalc(unittest.TestCase):

    def test_add(self):
        # docs.python.org/3/library/unittest.py
        result = test.add(10, 5)
        self.assertEqual(result, 14)


if __name__ == '__main__':  # run code within conditional - with unitttest.main
    unittest.main()
