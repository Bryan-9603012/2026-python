import sys


def build_prefix_by_char(grid, m, n):
    # 只針對網格中實際出現的字元建立 prefix sum，避免浪費空間。
    chars = set("".join(grid))
    prefix = {}

    for ch in chars:
        # ps[i + 1][j + 1] 表示左上角到 (i, j) 這塊區域中，字元 ch 出現的次數。
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_acc = 0
            for j in range(n):
                # 同一列累加目前字元 ch 的出現次數。
                if grid[i][j] == ch:
                    row_acc += 1
                ps[i + 1][j + 1] = ps[i][j + 1] + row_acc
        prefix[ch] = ps

    return prefix


def rect_sum(ps, r1, c1, r2, c2):
    # 利用二維 prefix sum，在 O(1) 算出矩形範圍內指定字元的數量。
    return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]


def largest_square(grid, prefix, m, n, r, c):
    # 中心點的字元就是整個正方形必須一致的目標字元。
    ch = grid[r][c]
    ps = prefix[ch]

    # 半徑不能超出上下左右邊界；邊長 = 半徑 * 2 + 1。
    max_radius = min(r, c, m - 1 - r, n - 1 - c)

    # 因為半徑越大條件越難成立，所以可以用二分搜尋找最大合法半徑。
    lo, hi = 0, max_radius
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        r1, c1 = r - mid, c - mid
        r2, c2 = r + mid, c + mid
        side = mid * 2 + 1
        area = side * side

        # 若矩形中目標字元數量等於面積，代表整個正方形都相同。
        if rect_sum(ps, r1, c1, r2, c2) == area:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return best * 2 + 1


def solve(data: str) -> str:
    # 以行為單位處理，因為網格本身是字串列，不能只用 split token。
    lines = data.splitlines()
    if not lines:
        return ""

    t = int(lines[0].strip())
    pos = 1
    out = []

    for _ in range(t):
        # 讀取 M、N、Q，並依照題目要求先輸出這三個數字。
        m, n, q = map(int, lines[pos].split())
        pos += 1
        grid = lines[pos:pos + m]
        pos += m

        # 預先建立每個字元的二維 prefix sum，讓每個查詢更快。
        prefix = build_prefix_by_char(grid, m, n)
        out.append(f"{m} {n} {q}")

        for _ in range(q):
            r, c = map(int, lines[pos].split())
            pos += 1
            out.append(str(largest_square(grid, prefix, m, n, r, c)))

    return "\n".join(out)


def main() -> None:
    # 一次讀入與一次輸出，減少 I/O 次數。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
