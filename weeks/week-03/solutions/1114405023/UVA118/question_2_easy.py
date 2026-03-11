def move_forward(x, y, direction):
    """
    根據目前方向，計算往前走一格後的新座標
    """
    if direction == 'N':
        return x, y + 1
    elif direction == 'S':
        return x, y - 1
    elif direction == 'E':
        return x + 1, y
    else:  # direction == 'W'
        return x - 1, y


def turn_left(direction):
    """
    左轉 90 度
    """
    if direction == 'N':
        return 'W'
    elif direction == 'W':
        return 'S'
    elif direction == 'S':
        return 'E'
    else:  # direction == 'E'
        return 'N'


def turn_right(direction):
    """
    右轉 90 度
    """
    if direction == 'N':
        return 'E'
    elif direction == 'E':
        return 'S'
    elif direction == 'S':
        return 'W'
    else:  # direction == 'W'
        return 'N'


def main():
    import sys

    # 讀入所有非空白行
    lines = [line.strip() for line in sys.stdin if line.strip()]

    # 第一行是地圖右上角座標
    x_max, y_max = map(int, lines[0].split())

    # 用來記錄 scent
    # 記錄格式：(x, y, direction)
    scents = set()

    index = 1

    # 後面每兩行是一台機器人
    while index < len(lines):
        # 讀入初始位置與方向
        x, y, direction = lines[index].split()
        x = int(x)
        y = int(y)

        # 讀入指令
        commands = lines[index + 1]

        # 記錄這台機器人是否掉出地圖
        lost = False

        # 逐一執行指令
        for command in commands:
            if command == 'L':
                direction = turn_left(direction)

            elif command == 'R':
                direction = turn_right(direction)

            elif command == 'F':
                # 先計算如果前進後會到哪裡
                new_x, new_y = move_forward(x, y, direction)

                # 如果前進後仍在地圖內，就真的移動
                if 0 <= new_x <= x_max and 0 <= new_y <= y_max:
                    x = new_x
                    y = new_y
                else:
                    # 如果前進後會掉出去，先檢查是否有 scent
                    if (x, y, direction) in scents:
                        # 有 scent：忽略這次危險前進
                        continue
                    else:
                        # 沒有 scent：這台機器人 LOST
                        scents.add((x, y, direction))
                        lost = True
                        break

        # 輸出結果
        if lost:
            print(x, y, direction, "LOST")
        else:
            print(x, y, direction)

        index += 2


if __name__ == "__main__":
    main()