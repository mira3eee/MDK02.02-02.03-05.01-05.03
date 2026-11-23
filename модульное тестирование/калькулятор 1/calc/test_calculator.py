"""Модульные тесты функций калькулятора."""

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.memory = {"value": 0}

    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(6, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(calculator.square_root(81), 9)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-9)

    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(calculator.factorial(0), 1)

    def test_factorial_invalid(self):
        with self.assertRaises(ValueError):
            calculator.factorial(2.5)

    def test_memory_store_and_read(self):
        calculator.memory_store(self.memory, 12)
        self.assertEqual(calculator.memory_read(self.memory), 12)

    def test_memory_read_empty(self):
        self.assertEqual(calculator.memory_read({}), 0)

    def test_memory_add(self):
        calculator.memory_store(self.memory, 10)
        calculator.memory_add(self.memory, 5)
        self.assertEqual(calculator.memory_read(self.memory), 15)

    def test_memory_clear(self):
        calculator.memory_store(self.memory, 10)
        calculator.memory_clear(self.memory)
        self.assertEqual(calculator.memory_read(self.memory), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
