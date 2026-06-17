"""
Week 17 - 0617 search.py 測試檔
"""

import unittest

from search import linear_search, binary_search


class TestSearchFunctions(unittest.TestCase):
    def test_linear_search_empty_list_should_return_minus_one(self):
        """空 list 找不到任何資料，應回傳 -1。"""
        self.assertEqual(linear_search([], 10), -1)

    def test_linear_search_find_first_item(self):
        """linear_search 可以找到第一個元素。"""
        self.assertEqual(linear_search([1, 2, 3], 1), 0)

    def test_linear_search_find_last_item(self):
        """linear_search 可以找到最後一個元素。"""
        self.assertEqual(linear_search([1, 2, 3], 3), 2)

    def test_linear_search_not_found(self):
        """linear_search 找不到時回傳 -1。"""
        self.assertEqual(linear_search([1, 2, 3], 99), -1)

    def test_binary_search_empty_list_should_return_minus_one(self):
        """空 list 進行 binary_search 時應回傳 -1。"""
        self.assertEqual(binary_search([], 10), -1)

    def test_binary_search_find_first_item(self):
        """binary_search 可以找到第一個元素。"""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_binary_search_find_last_item(self):
        """binary_search 可以找到最後一個元素。"""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_binary_search_not_found(self):
        """binary_search 找不到時回傳 -1。"""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 99), -1)

    def test_binary_search_unsorted_data_should_raise_value_error(self):
        """binary_search 收到未排序資料時應 raise ValueError。"""
        with self.assertRaises(ValueError):
            binary_search([3, 1, 2], 1)

    def test_search_should_not_modify_original_data(self):
        """linear_search 與 binary_search 都不可以修改原本的 data。"""
        data = [1, 2, 3, 4, 5]
        original = data.copy()

        linear_search(data, 3)
        binary_search(data, 3)

        self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
