import io
import sys
import unittest

# 匯入你的解答程式
import question_2


class TestUVA118(unittest.TestCase):
    def run_io_test(self, input_data: str, expected_output: str):
        """
        模擬 stdin / stdout 測試 main()。
        """
        backup_stdin = sys.stdin
        backup_stdout = sys.stdout

        try:
            sys.stdin = io.StringIO(input_data)
            sys.stdout = io.StringIO()

            question_2.main()

            actual_output = sys.stdout.getvalue()
            self.assertEqual(actual_output, expected_output)
        finally:
            sys.stdin = backup_stdin
            sys.stdout = backup_stdout

    def test_official_sample(self):
        """
        UVA 118 經典範例：
        第 1 台正常
        第 2 台 LOST
        第 3 台因為 scent 而避免掉落
        """
        input_data = """5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
"""
        expected_output = """1 1 E
3 3 N LOST
2 3 S
"""
        self.run_io_test(input_data, expected_output)

    def test_single_robot_lost(self):
        """
        單台機器人直接往外走，應輸出 LOST。
        """
        input_data = """1 1
1 1 E
F
"""
        expected_output = """1 1 E LOST
"""
        self.run_io_test(input_data, expected_output)

    def test_scent_prevents_second_loss(self):
        """
        第一台從 (1,1) 朝東掉落，留下 scent。
        第二台在相同位置、相同方向前進時，應忽略危險 F，不會 LOST。
        """
        input_data = """1 1
1 1 E
F
1 1 E
F
"""
        expected_output = """1 1 E LOST
1 1 E
"""
        self.run_io_test(input_data, expected_output)

    def test_turning_and_forward(self):
        """
        測試 L / R / F 的基本方向轉換。
        這組指令會讓機器人在第二次前進時掉出邊界。
        """
        input_data = """2 2
0 0 N
RFRFRFRF
"""
        expected_output = """1 0 S LOST
"""
        self.run_io_test(input_data, expected_output)

    def test_multiple_forward_inside_grid(self):
        """
        機器人在邊界內連續前進，不應 LOST。
        """
        input_data = """4 4
1 1 N
FFF
"""
        expected_output = """1 4 N
"""
        self.run_io_test(input_data, expected_output)

    def test_ignore_only_dangerous_forward(self):
        """
        scent 只會保護相同位置、相同方向的危險前進。
        第一台在 (2,2,N) 掉落。
        第二台雖然也從 (2,2) 出發，但先右轉成 E，
        所以危險方向不同，不會套用原本的 scent。
        """
        input_data = """2 2
2 2 N
F
2 2 N
RFRF
"""
        expected_output = """2 2 N LOST
2 2 E LOST
"""
        self.run_io_test(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()