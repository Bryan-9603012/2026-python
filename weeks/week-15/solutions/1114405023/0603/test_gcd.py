"""UVA 11417 GCD — 測試骨架"""

import unittest

from gcd import sum_of_gcd


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_2(self):
        # gcd(1,2) = 1
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_10(self):
        # UVA 11417 範例答案
        self.assertEqual(sum_of_gcd(10), 67)

    def test_edge_case_n_equals_1(self):
        # n=1 時沒有任何 1 <= i < j <= n 的組合
        self.assertEqual(sum_of_gcd(1), 0)

    def test_n_equals_3(self):
        # gcd(1,2)=1, gcd(1,3)=1, gcd(2,3)=1
        self.assertEqual(sum_of_gcd(3), 3)


if __name__ == "__main__":
    unittest.main()