import sys


def solve(data: str) -> str:
    # 將所有輸入一次讀入並切成 token，可減少逐行讀取的額外成本。
    tokens = data.split()
    if not tokens:
        return ""

    # 第一個數字是測資筆數。
    t = int(tokens[0])
    ans = []
    p = 1

    for _ in range(t):
        # 每筆測資包含 S（總和）與 D（差）。
        s = int(tokens[p])
        d = int(tokens[p + 1])
        p += 2

        # 兩隊分數分別為 (S + D) / 2 與 (S - D) / 2。
        # 有解條件：S >= D，且 S + D 必須是偶數，才會得到非負整數解。
        if s >= d and ((s + d) & 1) == 0:
            ans.append(f"{(s + d) // 2} {(s - d) // 2}")
        else:
            ans.append("impossible")

    # 一次組合輸出字串，比每行 print 更快。
    return "\n".join(ans)


def main() -> None:
    # UVA 題目通常使用標準輸入與標準輸出。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
