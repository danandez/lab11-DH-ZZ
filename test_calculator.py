# https://github.com/danandez/lab11-DH-ZZ
# Partner 1: Daniel Hernandez
# Partner 2: Zhijun Zhang
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 7), 7)
    def test_subtract(self):
        self.assertEqual(sub(8, 3), 5)
        self.assertEqual(sub(3, 8), -5)
        self.assertEqual(sub(0, 4), -4)
    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0,0) , 0)
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(-1, -1), 1)
        self.assertEqual(mul(6, -1), -6)

    def test_divide(self): # 3 assertions
        self.assertEqual(float(div(-1, -1)), 1.0)
        self.assertEqual(mul(0, 0), ZeroDivisionError)
        self.assertAlmostEqual(float(div(2,6)), 3.0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 1), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion #TODO: CONFIRM THIS WORKS
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(6,8), 10)
        self.assertEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(-9), ValueError)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(1), 1)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()