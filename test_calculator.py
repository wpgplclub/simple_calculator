
import unittest
from calculator import add, subtract, multiply


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiply(5, 3), 15)


if __name__ == "__main__":
    unittest.main()
