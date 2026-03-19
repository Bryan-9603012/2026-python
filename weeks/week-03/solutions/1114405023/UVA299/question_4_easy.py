def main():
    import sys

    # 讀入所有非空白行
    lines = [line.strip() for line in sys.stdin if line.strip()]

    # 第一行代表有幾組測資
    test_cases = int(lines[0])

    # 從第二行開始讀
    index = 1

    # 逐組處理
    for _ in range(test_cases):
        # 讀取車廂數量
        length = int(lines[index])

        # 讀取車廂排列
        train = list(map(int, lines[index + 1].split()))

        # 用來記錄交換次數
        swaps = 0

        # 這裡用 bubble sort 的概念
        # 每當前面的數比後面的大，就交換一次
        # 交換的總次數就是最少需要的相鄰交換次數
        for i in range(length):
            for j in range(0, length - 1 - i):
                if train[j] > train[j + 1]:
                    train[j], train[j + 1] = train[j + 1], train[j]
                    swaps += 1

        # 依照題目要求輸出格式
        print(f"Optimal train swapping takes {swaps} swaps.")

        # 下一組測資
        index += 2


if __name__ == "__main__":
    main()