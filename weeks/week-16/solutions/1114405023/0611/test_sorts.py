# test_sorts.py
import unittest

from sorts import (
    bubble_sort,
    quick_sort,
    merge_sort,
    builtin_sorted,
    optimized_quick_sort,
)


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.sort_functions = [
            bubble_sort,
            quick_sort,
            merge_sort,
            builtin_sorted,
            optimized_quick_sort,
        ]

    def test_sort_normal_integer_list(self):
        data = [5, 3, 8, 1, 2]
        expected = [1, 2, 3, 5, 8]

        for sort_func in self.sort_functions:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_empty_list(self):
        data = []
        expected = []

        for sort_func in self.sort_functions:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_single_element_list(self):
        data = [7]
        expected = [7]

        for sort_func in self.sort_functions:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_already_sorted_list(self):
        data = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]

        for sort_func in self.sort_functions:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_reverse_sorted_list(self):
        data = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]

        for sort_func in self.sort_functions:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_with_duplicate_values(self):
        data = [4, 2, 4, 1, 2]
        expected = [1, 2, 2, 4, 4]

        for sort_func in self.sort_functions:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_with_negative_numbers(self):
        data = [3, -1, 0, -5, 2]
        expected = [-5, -1, 0, 2, 3]

        for sort_func in self.sort_functions:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_should_not_modify_original_list(self):
        data = [3, 1, 2]
        original = data.copy()

        for sort_func in self.sort_functions:
            with self.subTest(sort_func=sort_func.__name__):
                result = sort_func(data)
                self.assertEqual(data, original)
                self.assertIsNot(result, data)

    def test_raise_type_error_when_input_is_not_list(self):
        invalid_data = "3, 1, 2"

        for sort_func in self.sort_functions:
            with self.subTest(sort_func=sort_func.__name__):
                with self.assertRaises(TypeError):
                    sort_func(invalid_data)


if __name__ == "__main__":
    unittest.main()