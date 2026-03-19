def main():
    import sys

    lines = [line.strip() for line in sys.stdin if line.strip()]
    t = int(lines[0])
    index = 1

    for _ in range(t):
        n = int(lines[index])
        train = list(map(int, lines[index + 1].split()))

        swaps = 0

        # 計算 inversion 數量
        for i in range(n):
            for j in range(i + 1, n):
                if train[i] > train[j]:
                    swaps += 1

        print(f"Optimal train swapping takes {swaps} swaps.")
        index += 2


if __name__ == "__main__":
    main()