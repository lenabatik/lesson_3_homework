from unittest import TestCase
import unittest
from calculator import Calculator
from genty import genty, genty_dataset

@genty
class CalculatorTestClass(TestCase):

    def setUp(self):
        self.calculator = Calculator()

    @genty_dataset((0, 9, 9), (2, 3, 5))
    def test_add_positive(self, x, y, result):
        self.assertEqual(self.calculator.add(x, y), result)

    @genty_dataset((0, 10, NotImplementedError), (-1, 9, NotImplementedError))
    def test_add_negative(self, x, y, result):
        self.assertRaises(result, lambda: self.calculator.add(x, y))

    @genty_dataset((0, 9, -9), (4, 3, 1))
    def test_subtract_positive(self, x, y, result):
        self.assertEqual(self.calculator.subtract(x, y), result)

    @genty_dataset((10, 0, NotImplementedError), (4, -1, NotImplementedError))
    def test_subtract_negative(self, x, y, result):
        self.assertRaises(result, lambda: self.calculator.subtract(x, y))

    @genty_dataset((0, 9, 0), (2, 3, 6))
    def test_multiply_positive(self, x, y, result):
        self.assertEqual(self.calculator.multiply(x, y), result)

    @genty_dataset((0, 10, NotImplementedError), (-1, 9, NotImplementedError))
    def test_multiply_negative(self, x, y, result):
        self.assertRaises(result, lambda: self.calculator.multiply(x, y))

    @genty_dataset((0, 9, 0), (5, 2, 2.5), (8, 2, 4))
    def test_divide_positive(self, x, y, result):
        self.assertEqual(self.calculator.divide(x, y), result)

    @genty_dataset((10, 1, NotImplementedError), (-1, 9, NotImplementedError), (5, 0, ZeroDivisionError))
    def test_divide_negative(self, x, y, result):
        self.assertRaises(result, lambda: self.calculator.divide(x, y))

    @genty_dataset(('2*3', 6), ('2*2+3', 7), (('2*(2+3)', 10)), ('2/(9-5)', 0.5))
    def test_evaluate_positive(self, x, result):
        self.assertEqual(self.calculator.evaluate(x), result)

    @genty_dataset(('(2*(2+3, 7)', SyntaxError), ('4/0', ZeroDivisionError))
    def test_evaluate_negative(self, x, result):
        self.assertRaises(result, lambda: self.calculator.evaluate(x))


if __name__ == '__main__':
    unittest.main()