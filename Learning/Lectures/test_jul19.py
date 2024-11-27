from unittest import TestCase
from jul19 import *


class Test(TestCase):
    def test_zero(self):
        self.assertEqual(calculate_area(0,5),0)

    def test_positive_integers(self):
        self.assertEqual(calculate_area(1,4),4)

    def test_negative_nums(self):
        self.assertEqual(calculate_area(-5,4),-20)

    def test_floating_point(self):
        self.assertEqual(calculate_area(2.5,3.5),8.75)