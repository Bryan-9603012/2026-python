import unittest

from digit_root import digit_root

class TestDigitRoot(unittest.TestCase):

    def test_single_digit_returns_itself(self):
        self.assertEqual(digit_root(7), 7)

    def test_multiple_rounds_digit_root(self):
        self.assertEqual(digit_root(199), 1)

    def test_large_number(self):
        self.assertEqual(digit_root(2000000000), 2)

    def test_edge_case_minimum_valid_number(self):
        self.assertEqual(digit_root(1), 1)

    def test_raises_value_error_when_less_than_one(self):
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(0)
    
    def test_raises_value_error_when_not_an_integer(self):
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(-1)

if "__name__" == "__main__":
    unittest.main()
