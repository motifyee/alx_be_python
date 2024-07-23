import unittest
from simple_calculator import SimpleCalculator


class TestCalc(unittest.TestCase):
    def test_addition(self):
        res = SimpleCalculator().add(222, 333)
        self.assertEqual(res, 555)

    def test_subtraction(self):
        res = SimpleCalculator().subtract(333, 222)
        self.assertEqual(res, 100)

    def test_multiply(self):
        res = SimpleCalculator().multiply(10, 20)
        self.assertEqual(res, 200)

    def test_divide(self):
        res = SimpleCalculator().divide(90, 10)
        self.assertEqual(res, 9)

        with self.assertRaises(ZeroDivisionError):
            SimpleCalculator().divide(90, 0)


if __name__ == "__main__":
    unittest.main()
