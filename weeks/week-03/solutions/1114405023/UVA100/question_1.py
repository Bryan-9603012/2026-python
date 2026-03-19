memo = {1: 1}


def cycle_length(n: int) -> int:
    """
    計算單一數字 n 的 cycle length
    使用記憶化避免重複計算
    """
    if n in memo:
        return memo[n]

    if n % 2 == 0:
        result = 1 + cycle_length(n // 2)
    else:
        result = 1 + cycle_length(3 * n + 1)

    memo[n] = result
    return result


def max_cycle_length(i: int, j: int) -> int:
    """
    找出區間 [min(i, j), max(i, j)] 中最大的 cycle length
    """
    left = min(i, j)
    right = max(i, j)

    max_len = 0
    for n in range(left, right + 1):
        length = cycle_length(n)
        if length > max_len:
            max_len = length

    return max_len


def main():
    """
    從標準輸入讀入多組 i j
    輸出格式：i j max_cycle_length
    """
    import sys

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        i, j = map(int, line.split())
        ans = max_cycle_length(i, j)
        print(i, j, ans)


if __name__ == "__main__":
    main()