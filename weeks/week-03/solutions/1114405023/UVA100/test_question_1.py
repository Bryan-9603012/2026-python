import io
import sys
import unittest
import question_1


class TestUVA100(unittest.TestCase):
    def run_io_test(self, input_data: str, expected_output: str):
        backup_stdin = sys.stdin
        backup_stdout = sys.stdout

        try:
            sys.stdin = io.StringIO(input_data)
            sys.stdout = io.StringIO()

            question_1.main()

            actual_output = sys.stdout.getvalue()
            self.assertEqual(actual_output, expected_output)
        finally:
            sys.stdin = backup_stdin
            sys.stdout = backup_stdout

    def test_sample_case(self):
        input_data = """1 10
100 200
201 210
900 1000
"""
        expected_output = """1 10 20
100 200 125
201 210 89
900 1000 174
"""
        self.run_io_test(input_data, expected_output)

    def test_same_number(self):
        input_data = "1 1\n"
        expected_output = "1 1 1\n"
        self.run_io_test(input_data, expected_output)

    def test_reverse_range(self):
        input_data = "10 1\n"
        expected_output = "10 1 20\n"
        self.run_io_test(input_data, expected_output)

    def test_small_range(self):
        input_data = "5 10\n"
        expected_output = "5 10 20\n"
        self.run_io_test(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()