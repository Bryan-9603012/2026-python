import os
import sys
import unittest

# 讓 tests 可以正確匯入上一層的 robot_core.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from robot_core import turn_left, turn_right


class TestRobotCore(unittest.TestCase):
    def test_turn_left_from_north(self):
        self.assertEqual(turn_left("N"), "W")

    def test_turn_left_from_west(self):
        self.assertEqual(turn_left("W"), "S")

    def test_turn_left_from_south(self):
        self.assertEqual(turn_left("S"), "E")

    def test_turn_left_from_east(self):
        self.assertEqual(turn_left("E"), "N")

    def test_turn_right_from_north(self):
        self.assertEqual(turn_right("N"), "E")

    def test_turn_right_from_east(self):
        self.assertEqual(turn_right("E"), "S")

    def test_turn_right_from_south(self):
        self.assertEqual(turn_right("S"), "W")

    def test_turn_right_from_west(self):
        self.assertEqual(turn_right("W"), "N")

    def test_turn_left_four_times_back_to_original(self):
        direction = "N"
        for _ in range(4):
            direction = turn_left(direction)
        self.assertEqual(direction, "N")

    def test_turn_right_four_times_back_to_original(self):
        direction = "N"
        for _ in range(4):
            direction = turn_right(direction)
        self.assertEqual(direction, "N")


if __name__ == "__main__":
    unittest.main()