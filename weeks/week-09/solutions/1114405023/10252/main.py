import sys

def solve_case(points: list[tuple[int, int]]) -> tuple[int, int]:
    xs = sorted(x for x, _ in points)
    ys = sorted(y for _, y in points)
    n = len(points)

    if n % 2 == 1:
        x1 = x2 = xs[n // 2]
        y1 = y2 = ys[n // 2]
    else:
        x1, x2 = xs[n // 2 - 1], xs[n // 2]
        y1, y2 = ys[n // 2 - 1], ys[n // 2]

    dist = sum(abs(x - x1) for x in xs) + sum(abs(y - y1) for y in ys)
    cnt = (x2 - x1 + 1) * (y2 - y1 + 1)
    return dist, cnt

def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    t = nums[0]
    idx = 1
    out = []
    for _ in range(t):
        n = nums[idx]
        idx += 1
        pts = []
        for _ in range(n):
            pts.append((nums[idx], nums[idx + 1]))
            idx += 2
        dist, cnt = solve_case(pts)
        out.append(f'{dist} {cnt}')
    return '\n'.join(out)

if __name__ == '__main__':
    print(solve(sys.stdin.read()), end='')
