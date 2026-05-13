import sys

def build_prefix_by_char(grid, m, n):
    chars = set("".join(grid))
    prefix = {}

    for ch in chars:
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_acc = 0

            for j in range(n):
                if grid[i][j] == ch:
                    row_acc += 1
                ps[i + 1][j + 1] = ps[i][j + 1] + row_acc
        prefix[ch] = ps
    return prefix





def rect_sum(ps, r1, c1, r2, c2):
    return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]





def largest_square(grid, prefix, m, n, r, c):
    ch = grid[r][c]
    ps = prefix[ch]
    max_radius = min(r, c, m - 1 - r, n - 1 - c)
    lo, hi = 0, max_radius
    best = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        r1, c1 = r - mid, c - mid
        r2, c2 = r + mid, c + mid
        side = mid * 2 + 1
        area = side * side

        if rect_sum(ps, r1, c1, r2, c2) == area:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return best * 2 + 1


def solve(data: str) -> str:



    lines = data.splitlines()

    if not lines:

        return ""



    t = int(lines[0].strip())

    pos = 1

    out = []



    for _ in range(t):



        m, n, q = map(int, lines[pos].split())

        pos += 1

        grid = lines[pos:pos + m]

        pos += m





        prefix = build_prefix_by_char(grid, m, n)

        out.append(f"{m} {n} {q}")



        for _ in range(q):

            r, c = map(int, lines[pos].split())

            pos += 1

            out.append(str(largest_square(grid, prefix, m, n, r, c)))



    return "\n".join(out)





def main() -> None:



    sys.stdout.write(solve(sys.stdin.read()))





if __name__ == "__main__":

    main()
