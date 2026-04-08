import sys


def solve(data: str) -> str:
    # 讀入輸入資料
    parts = data.strip().split()
    if not parts:
        return ""

    # n = 集合大小，s = 集合內容
    n = int(parts[0])
    s = list(map(int, parts[1:1 + n]))

    # 簡單版：直接暴力枚舉 a, b, c, d, e, f
    # 檢查 a+b+c+d+e 是否等於 f
    ans = 0
    for a in s:
        for b in s:
            for c in s:
                for d in s:
                    for e in s:
                        for f in s:
                            if a + b + c + d + e == f:
                                ans += 1

    return str(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
