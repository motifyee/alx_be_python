import unittest
from simple_calculator import SimpleCalculator


class TestCalc(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(222, 333), 555)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(333, 222), 100)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 20), 200)

    def test_division(self):
        self.assertEqual(self.calc.divide(90, 10), 9)
        self.assertEqual(self.calc.divide(90, 0), None)

        # with self.assertRaises(ZeroDivisionError):
        #     SimpleCalculator().divide(90, 0)


if __name__ == "__main__":
    unittest.main()
