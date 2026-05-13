import sys


def is_multiple_of_11(num: str) -> bool:
    # 11 倍數規則：奇數位與偶數位數字和的差若可被 11 整除，原數也是 11 的倍數。
    diff = 0
    sign = 1
    for ch in num:
        # sign 在 +1 與 -1 之間切換，等同於交錯加減每一位數字。
        diff += sign * (ord(ch) - 48)
        sign = -sign

    return diff % 11 == 0


def solve(data: str) -> str:
    ans = []
    for num in data.split():
        # 題目規定輸入 0 代表結束。
        if num == "0":
            break

        # 依照判斷結果決定是否在句子中加入 not。
        word = "" if is_multiple_of_11(num) else " not"
        ans.append(f"{num} is{word} a multiple of 11.")

    return "\n".join(ans)


def main() -> None:
    # 一次讀取所有輸入並輸出結果。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
