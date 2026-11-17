import unittest

from calculator import calculator


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator("add", 5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(calculator("subtract", 5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculator("multiply", -5, 3), -15)

    def test_division(self):
        self.assertEqual(calculator("divide", 5, 2), 2.5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculator("divide", 5, 0)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculator("invalid", 5, 3)


if __name__ == "__main__":
    unittest.main()
