class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.lost = False


def turn_left(direction):
    left_map = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }
    return left_map[direction]


def turn_right(direction):
    right_map = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }
    return right_map[direction]


def move_forward(x, y, direction):
    if direction == 'N':
        return x, y + 1
    elif direction == 'S':
        return x, y - 1
    elif direction == 'E':
        return x + 1, y
    elif direction == 'W':
        return x - 1, y
    else:
        raise ValueError(f"Invalid direction: {direction}")


def is_out_of_bounds(x, y, x_max, y_max):
    return x < 0 or x > x_max or y < 0 or y > y_max


def execute_command(robot, command, x_max, y_max, scents):
    if robot.lost:
        return

    if command == 'L':
        robot.direction = turn_left(robot.direction)

    elif command == 'R':
        robot.direction = turn_right(robot.direction)

    elif command == 'F':
        new_x, new_y = move_forward(robot.x, robot.y, robot.direction)

        if is_out_of_bounds(new_x, new_y, x_max, y_max):
            scent_key = (robot.x, robot.y, robot.direction)

            if scent_key in scents:
                return

            scents.add(scent_key)
            robot.lost = True
        else:
            robot.x = new_x
            robot.y = new_y

    else:
        raise ValueError(f"Invalid command: {command}")


def execute_commands(robot, commands, x_max, y_max, scents):
    for command in commands:
        if robot.lost:
            break
        execute_command(robot, command, x_max, y_max, scents)


def format_robot_output(robot):
    if robot.lost:
        return f"{robot.x} {robot.y} {robot.direction} LOST"
    return f"{robot.x} {robot.y} {robot.direction}"


def main():
    import sys

    lines = [line.strip() for line in sys.stdin if line.strip()]
    x_max, y_max = map(int, lines[0].split())
    scents = set()

    index = 1
    while index < len(lines):
        x, y, direction = lines[index].split()
        x = int(x)
        y = int(y)
        commands = lines[index + 1]

        robot = Robot(x, y, direction)
        execute_commands(robot, commands, x_max, y_max, scents)
        print(format_robot_output(robot))

        index += 2


if __name__ == "__main__":
    main()