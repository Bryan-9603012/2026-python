def move_forward(x, y, direction):
    """
    根據目前方向，計算往前走一格後的新座標
    只負責計算，不負責判斷是否超出邊界
    """
    if direction == 'N':
        return x, y + 1
    elif direction == 'S':
        return x, y - 1
    elif direction == 'E':
        return x + 1, y
    elif direction == 'W':
        return x - 1, y


def turn_left(direction):
    """
    左轉 90 度後的新方向
    """
    left_map = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }
    return left_map[direction]


def turn_right(direction):
    """
    右轉 90 度後的新方向
    """
    right_map = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }
    return right_map[direction]


def main():
    import sys

    # 讀入所有非空白行
    # 第 1 行是地圖右上角座標
    # 後面每 2 行代表一台機器人：
    # 第 1 行 = 初始位置與方向
    # 第 2 行 = 指令字串
    lines = [line.strip() for line in sys.stdin if line.strip()]

    # 地圖範圍：左下角固定是 (0, 0)，右上角是 (x_max, y_max)
    x_max, y_max = map(int, lines[0].split())

    # scent 用來記錄：
    # 哪個位置 + 哪個方向 曾經發生過「往前會掉出去」
    # 之後若別台機器人在相同情況下再收到 F，就要忽略這次 F
    scents = set()

    # 從第 2 行開始處理每台機器人
    index = 1

    while index < len(lines):
        # 讀取機器人的初始位置與方向
        x, y, direction = lines[index].split()
        x = int(x)
        y = int(y)

        # 讀取這台機器人的指令
        commands = lines[index + 1]

        # 紀錄這台機器人是否掉出地圖
        lost = False

        # 逐一執行指令
        for cmd in commands:
            if cmd == 'L':
                # 左轉
                direction = turn_left(direction)

            elif cmd == 'R':
                # 右轉
                direction = turn_right(direction)

            elif cmd == 'F':
                # 先計算如果往前走，會到哪裡
                nx, ny = move_forward(x, y, direction)

                # 如果新位置仍在地圖內，就真的移動
                if 0 <= nx <= x_max and 0 <= ny <= y_max:
                    x, y = nx, ny

                else:
                    # 如果往前會掉出地圖，先檢查是否有 scent
                    if (x, y, direction) in scents:
                        # 有 scent：表示之前已有機器人在這裡、朝這個方向掉下去
                        # 所以這次 F 要忽略，不移動、不中斷，直接看下一個指令
                        continue
                    else:
                        # 沒有 scent：這台機器人會 LOST
                        # 並在目前位置與方向留下 scent
                        scents.add((x, y, direction))
                        lost = True
                        break

        # 依照是否 LOST 來輸出結果
        if lost:
            print(x, y, direction, "LOST")
        else:
            print(x, y, direction)

        # 下一台機器人從再後面兩行開始
        index += 2


if __name__ == "__main__":
    main()