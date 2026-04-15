import sys

DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

def solve(data: str) -> str:
    lines = data.strip().splitlines()
    idx = 0
    case_no = 1
    out = []

    while idx < len(lines):
        n, m = map(int, lines[idx].split())
        idx += 1
        if n == 0 and m == 0:
            break

        grid = [list(lines[idx + i].rstrip()) for i in range(n)]
        idx += n

        ans = [['0'] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '*':
                    ans[r][c] = '*'
                    continue
                count = 0
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
                        count += 1
                ans[r][c] = str(count)

        if case_no > 1:
            out.append("")
        out.append(f"Field #{case_no}:")
        out.extend("".join(row) for row in ans)
        case_no += 1

    return "\n".join(out)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
