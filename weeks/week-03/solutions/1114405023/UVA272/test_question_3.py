import io
import sys
import unittest

# 匯入你的正式解答程式
import question_3


class TestUVA272(unittest.TestCase):
    def run_io_test(self, input_data: str, expected_output: str):
        """
        模擬 stdin / stdout，測試 question_3.main() 的輸出是否正確。
        """
        backup_stdin = sys.stdin
        backup_stdout = sys.stdout

        try:
            sys.stdin = io.StringIO(input_data)
            sys.stdout = io.StringIO()

            question_3.main()

            actual_output = sys.stdout.getvalue()
            self.assertEqual(actual_output, expected_output)
        finally:
            sys.stdin = backup_stdin
            sys.stdout = backup_stdout

    def test_official_sample(self):
        """
        測試題目經典範例。
        """
        input_data = '''"To be or not to be," quoth the Bard, "that is the question".
The programming contestant replied: "I must disagree.
To `C' or not to `C', that is The Question!"
'''
        expected_output = """``To be or not to be,'' quoth the Bard, ``that is the question''.
The programming contestant replied: ``I must disagree.
To `C' or not to `C', that is The Question!''
"""
        self.run_io_test(input_data, expected_output)

    def test_no_quotes(self):
        """
        沒有雙引號時，內容應保持不變。
        """
        input_data = """Hello World
Python is fun
"""
        expected_output = """Hello World
Python is fun
"""
        self.run_io_test(input_data, expected_output)

    def test_single_pair_quotes(self):
        """
        單一組雙引號測試。
        """
        input_data = '''"Hello, world!"
'''
        expected_output = """``Hello, world!''
"""
        self.run_io_test(input_data, expected_output)

    def test_multiple_pairs_same_line(self):
        """
        同一行有多組雙引號，應交替替換。
        """
        input_data = '''"A" "B" "C"
'''
        expected_output = """``A'' ``B'' ``C''
"""
        self.run_io_test(input_data, expected_output)

    def test_quotes_across_lines(self):
        """
        引號開關狀態需要跨行延續，不能每一行重置。
        """
        input_data = '''"Hello
world"
'''
        expected_output = """``Hello
world''
"""
        self.run_io_test(input_data, expected_output)

    def test_mixed_text(self):
        """
        測試一般文字與雙引號混合的情況。
        """
        input_data = '''She said, "Hi", and then he said, "Bye".
'''
        expected_output = """She said, ``Hi'', and then he said, ``Bye''.
"""
        self.run_io_test(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()