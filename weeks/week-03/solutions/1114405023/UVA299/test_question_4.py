import io
import sys
import unittest

# 匯入你的正式解答程式
import question_4


class TestUVA299(unittest.TestCase):
    def run_io_test(self, input_data: str, expected_output: str):
        """
        模擬 stdin / stdout，測試 question_4.main() 的輸出是否正確。
        """
        backup_stdin = sys.stdin
        backup_stdout = sys.stdout

        try:
            sys.stdin = io.StringIO(input_data)
            sys.stdout = io.StringIO()

            question_4.main()

            actual_output = sys.stdout.getvalue()
            self.assertEqual(actual_output, expected_output)
        finally:
            sys.stdin = backup_stdin
            sys.stdout = backup_stdout

    def test_official_sample(self):
        """
        測試題目範例。
        """
        input_data = """3
3
1 3 2
4
4 3 2 1
2
2 1
"""
        expected_output = """Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 1 swaps.
"""
        self.run_io_test(input_data, expected_output)

    def test_already_sorted(self):
        """
        已經排序好的情況，不需要交換。
        """
        input_data = """1
5
1 2 3 4 5
"""
        expected_output = """Optimal train swapping takes 0 swaps.
"""
        self.run_io_test(input_data, expected_output)

    def test_reverse_sorted(self):
        """
        完全反序時，交換次數最多。
        例如 5 4 3 2 1，共需 10 次交換。
        """
        input_data = """1
5
5 4 3 2 1
"""
        expected_output = """Optimal train swapping takes 10 swaps.
"""
        self.run_io_test(input_data, expected_output)

    def test_single_carriage(self):
        """
        只有一節車廂時，不需要交換。
        """
        input_data = """1
1
1
"""
        expected_output = """Optimal train swapping takes 0 swaps.
"""
        self.run_io_test(input_data, expected_output)

    def test_small_case(self):
        """
        小型測資測試。
        3 1 2 -> 需要 2 次交換
        """
        input_data = """1
3
3 1 2
"""
        expected_output = """Optimal train swapping takes 2 swaps.
"""
        self.run_io_test(input_data, expected_output)

    def test_multiple_cases(self):
        """
        多組測資一起測試。
        """
        input_data = """2
3
2 1 3
4
2 4 1 3
"""
        expected_output = """Optimal train swapping takes 1 swaps.
Optimal train swapping takes 3 swaps.
"""
        self.run_io_test(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()