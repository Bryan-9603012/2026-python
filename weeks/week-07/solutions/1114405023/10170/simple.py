import sys


def solve(data: str) -> str:
    out = []

    # 題目有多筆測資，逐行處理直到 EOF
    for line in data.strip().splitlines():
        line = line.strip()
        if not line:
            continue

        # s = 第一個旅行團人數
        # d = 要查詢第幾天
        s, d = map(int, line.split())

        # cur = 目前旅行團的人數
        # days = 累積到目前為止已經住掉幾天
        cur = s
        days = 0

        # 簡單版直接模擬
        # 人數為 cur 的旅行團會住 cur 天
        while True:
            days += cur
            if days >= d:
                out.append(str(cur))
                break
            cur += 1

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
