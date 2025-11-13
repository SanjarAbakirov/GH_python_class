import unittest
import test


class TestCalc(unittest.TestCase):

    def test_add(self):
        # docs.python.org/3/library/unittest.py
        result = test.add(10, 5)
        self.assertEqual(result, 15)
