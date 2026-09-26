import unittest

from sum_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_add_two_integers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_two_floats(self):
        self.assertEqual(add_numbers(1.5, 2.5), 4.0)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-4, 4), 0)

    def test_add_int_and_float(self):
        self.assertEqual(add_numbers(1, 2.5), 3.5)


if __name__ == "__main__":
    unittest.main()
