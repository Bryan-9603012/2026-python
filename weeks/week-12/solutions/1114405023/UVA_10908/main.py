import sys


def largest_square(grid, m, n, r, c):
    target = grid[r][c]
    radius = 0

    while True:
        nr = radius + 1
        top = r - nr
        bottom = r + nr
        left = c - nr
        right = c + nr

        if top < 0 or bottom >= m or left < 0 or right >= n:
            break

        ok = True
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                if grid[i][j] != target:
                    ok = False
                    break
            if not ok:
                break

        if not ok:
            break
        radius = nr

    return radius * 2 + 1


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
        out.append(f"{m} {n} {q}")

        for _ in range(q):
            r, c = map(int, lines[pos].split())
            pos += 1
            out.append(str(largest_square(grid, m, n, r, c)))

    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
