import sys


def to_binary_and_count_ones(n: int):
    # bits 用來存二進位位元；ones 用來統計 1 的個數。
    bits = []
    ones = 0

    while n > 0:
        # n & 1 可以取得目前最低位元。
        bit = n & 1
        if bit:
            ones += 1
        bits.append(str(bit))

        # 右移一位，相當於整數除以 2。
        n >>= 1

    # 因為是從最低位元往最高位元取出，所以最後要反轉。
    return "".join(reversed(bits)), ones


def solve(data: str) -> str:
    ans = []
    for token in data.split():
        n = int(token)
        # 題目規定輸入 0 時結束，不輸出結果。
        if n == 0:
            break

        binary, ones = to_binary_and_count_ones(n)
        ans.append(f"The parity of {binary} is {ones} (mod 2).")

    return "\n".join(ans)


def main() -> None:
    # 使用標準輸入與標準輸出，符合 UVA 評測格式。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
