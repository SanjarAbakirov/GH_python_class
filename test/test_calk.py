import unittest
import test


class TestCalc(unittest.TestCase):

    def test_add(self):
        # docs.python.org/3/library/unittest.py
        # result = test.add(10, 5)
        # self.assertEqual(result, 15)
        self.assertEqual(test.add(10, 5), 15)
        self.assertEqual(test.add(1, -1), 0)
        self.assertEqual(test.add(-1, -1), -2)
        self.assertEqual(test.add(10, 9), 19)


if __name__ == '__main__':  # run code within conditional - with unitttest.main
    unittest.main()
