def main():
    import sys

    # 讀入所有行，保留每行原本的內容
    # 只去掉每行最後的換行符號
    lines = [line.rstrip("\n") for line in sys.stdin]

    # 如果沒有輸入資料，就直接結束
    if not lines:
        return

    # 找出最長那一行的長度
    max_length = 0
    for line in lines:
        if len(line) > max_length:
            max_length = len(line)

    # 題目要把整份文字順時針旋轉 90 度
    # 旋轉後的新第 1 行，來自原本所有行的第 1 個字元（由下往上讀）
    # 旋轉後的新第 2 行，來自原本所有行的第 2 個字元（由下往上讀）
    # 以此類推
    for col in range(max_length):
        new_line = ""

        # 由最後一行往第一行掃描
        for row in range(len(lines) - 1, -1, -1):
            # 如果這一行有第 col 個字元，就取出來
            if col < len(lines[row]):
                new_line += lines[row][col]
            else:
                # 如果沒有，就補空白
                new_line += " "

        # 題目輸出通常不需要保留行尾多餘空白
        print(new_line.rstrip())


if __name__ == "__main__":
    main()