def get_cycle_length(n):
    """
    計算單一數字 n 的 cycle length
    """
    length = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1

    return length


def main():
    import sys

    # 題目會有多組輸入，直到 EOF 結束
    for line in sys.stdin:
        line = line.strip()

        # 如果遇到空行就跳過
        if not line:
            continue

        # 讀入一組 i, j
        i, j = map(int, line.split())

        # 題目要求輸出原本輸入順序
        original_i = i
        original_j = j

        # 計算時要用較小到較大的範圍
        start = min(i, j)
        end = max(i, j)

        # 記錄最大 cycle length
        max_cycle_length = 0

        # 對區間內每個數字都計算 cycle length
        for number in range(start, end + 1):
            cycle_length = get_cycle_length(number)

            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length

        # 依照題目格式輸出
        print(original_i, original_j, max_cycle_length)


if __name__ == "__main__":
    main()