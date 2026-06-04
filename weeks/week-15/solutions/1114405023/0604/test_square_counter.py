"""平方數計數 — 測試檔

題目：count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
      若 a > b，應 raise ValueError("a must be <= b")。
"""

import unittest

from square_counter import count_squares


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        # [1, 10] 裡的完全平方數是 1, 4, 9
        self.assertEqual(count_squares(1, 10), 3)

    def test_single_point_square(self):
        # edge case: 單點區間，且該數是完全平方數
        self.assertEqual(count_squares(9, 9), 1)

    def test_single_point_not_square(self):
        # edge case: 單點區間，但該數不是完全平方數
        self.assertEqual(count_squares(8, 8), 0)

    def test_invalid_input_raises(self):
        # a > b 時應該丟 ValueError
        with self.assertRaises(ValueError):
            count_squares(5, 2)


if __name__ == "__main__":
    unittest.main()