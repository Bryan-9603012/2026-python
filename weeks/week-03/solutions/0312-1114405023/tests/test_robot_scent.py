import os
import sys
import unittest

# 讓 tests 可以匯入上一層 robot_core.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from robot_core import Robot, execute_command, execute_commands, move_forward, is_out_of_bounds


class TestRobotScent(unittest.TestCase):
    def test_move_forward_north(self):
        self.assertEqual(move_forward(1, 1, 'N'), (1, 2))

    def test_move_forward_east(self):
        self.assertEqual(move_forward(1, 1, 'E'), (2, 1))

    def test_is_out_of_bounds_true(self):
        self.assertTrue(is_out_of_bounds(6, 3, 5, 3))

    def test_is_out_of_bounds_false(self):
        self.assertFalse(is_out_of_bounds(5, 3, 5, 3))

    def test_robot_moves_forward_inside_grid(self):
        robot = Robot(1, 1, 'N')
        scents = set()
        execute_command(robot, 'F', 5, 3, scents)
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (1, 2, 'N', False))

    def test_robot_becomes_lost_when_moving_out_of_bounds(self):
        robot = Robot(3, 3, 'N')
        scents = set()
        execute_command(robot, 'F', 5, 3, scents)
        self.assertTrue(robot.lost)
        self.assertIn((3, 3, 'N'), scents)

    def test_second_robot_ignores_scented_danger(self):
        robot = Robot(3, 3, 'N')
        scents = {(3, 3, 'N')}
        execute_command(robot, 'F', 5, 3, scents)
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (3, 3, 'N', False))

    def test_same_position_different_direction_not_protected_by_scent(self):
        robot = Robot(3, 3, 'E')
        scents = {(3, 3, 'N')}
        execute_command(robot, 'F', 3, 3, scents)
        self.assertTrue(robot.lost)

    def test_robot_stops_after_lost(self):
        robot = Robot(3, 3, 'N')
        scents = set()
        execute_commands(robot, 'FRF', 5, 3, scents)
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (3, 3, 'N', True))

    def test_invalid_command_raises_value_error(self):
        robot = Robot(1, 1, 'N')
        scents = set()
        with self.assertRaises(ValueError):
            execute_command(robot, 'X', 5, 3, scents)


if __name__ == "__main__":
    unittest.main()