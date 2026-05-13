import sys


def sum_digits_text(text: str) -> int:
    # 以字串逐字元加總，避免超大整數轉 int 造成限制或額外成本。
    return sum(ord(ch) - 48 for ch in text)


def nine_degree(num: str) -> int:
    # 先計算原數字的 digit sum；若不是 9 的倍數，直接回傳 0。
    current = sum_digits_text(num)
    if current % 9 != 0:
        return 0

    # 能被 9 整除時，第一次 digit sum 就算第 1 層 9-degree。
    degree = 1
    while current != 9:
        # 若加總結果還不是 9，就繼續對加總結果做 digit sum。
        current = sum_digits_text(str(current))
        degree += 1

    return degree


def solve(data: str) -> str:
    ans = []
    for num in data.split():
        # 題目規定輸入 0 代表結束，不需要輸出。
        if num == "0":
            break

        degree = nine_degree(num)
        if degree == 0:
            ans.append(f"{num} is not a multiple of 9.")
        else:
            ans.append(f"{num} is a multiple of 9 and has 9-degree {degree}.")

    return "\n".join(ans)


def main() -> None:
    # 使用 stdin/stdout 符合線上評測格式。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
