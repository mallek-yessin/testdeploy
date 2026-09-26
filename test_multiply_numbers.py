import unittest

from multiply_numbers import multiply_numbers


class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_two_integers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

    def test_multiply_two_floats(self):
        self.assertEqual(multiply_numbers(1.5, 2.5), 3.75)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_numbers(-4, 4), -16)

    def test_multiply_int_and_float(self):
        self.assertEqual(multiply_numbers(1, 2.5), 2.5)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply_numbers(0, 7), 0)


if __name__ == "__main__":
    unittest.main()
