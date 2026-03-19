import io
import sys
import unittest

# 匯入你的正式解答程式
import question_5


class TestUVA490(unittest.TestCase):
    def run_io_test(self, input_data: str, expected_output: str):
        backup_stdin = sys.stdin
        backup_stdout = sys.stdout

        try:
            sys.stdin = io.StringIO(input_data)
            sys.stdout = io.StringIO()

            question_5.main()

            actual_output = sys.stdout.getvalue()
            self.assertEqual(actual_output, expected_output)
        finally:
            sys.stdin = backup_stdin
            sys.stdout = backup_stdout

    def test_simple_square(self):
        """
        簡單的 2x2 旋轉測試。
        """
        input_data = """ab
cd
"""
        expected_output = """ca
db
"""
        self.run_io_test(input_data, expected_output)

    def test_uneven_lines(self):
        """
        每行長度不同時，需先補空白再旋轉。
        """
        input_data = """ABC
DE
F
"""
        expected_output = """FDA
 EB
  C
"""
        self.run_io_test(input_data, expected_output)

    def test_single_line(self):
        """
        只有一行時，旋轉後會變成直排。
        """
        input_data = """HELLO
"""
        expected_output = """H
E
L
L
O
"""
        self.run_io_test(input_data, expected_output)

    def test_single_character_lines(self):
        """
        多行單字元測試。
        """
        input_data = """A
B
C
"""
        expected_output = """CBA
"""
        self.run_io_test(input_data, expected_output)

    def test_with_spaces_in_text(self):
        """
        文字中本來就有空白時，應正常保留。
        """
        input_data = """I love
Python
"""
        expected_output = """PI
yl
to
hv
oe
 n
"""
        self.run_io_test(input_data, expected_output)

    def test_empty_input(self):
        """
        空輸入時，不應輸出任何內容。
        """
        input_data = ""
        expected_output = ""
        self.run_io_test(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()