import unittest
from unittest import TestCase
from jul17 import *


class Test(TestCase):
    def test_calc_avg(self):
        self.assertEqual(calc_avg([3,3,3]),3)

if __name__ == '__main__':
    unittest.main()