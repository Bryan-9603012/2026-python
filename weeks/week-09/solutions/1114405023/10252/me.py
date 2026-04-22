import sys

a = list(map(int, sys.stdin.read().split()))
t = a[0]
p = 1
ans = []
for _ in range(t):
    n = a[p]
    p += 1
    xs, ys = [], []
    for _ in range(n):
        xs.append(a[p])
        ys.append(a[p + 1])
        p += 2
    xs.sort()
    ys.sort()
    if n % 2:
        lx = rx = xs[n // 2]
        ly = ry = ys[n // 2]
    else:
        lx, rx = xs[n // 2 - 1], xs[n // 2]
        ly, ry = ys[n // 2 - 1], ys[n // 2]
    s = sum(abs(x - lx) for x in xs) + sum(abs(y - ly) for y in ys)
    cnt = (rx - lx + 1) * (ry - ly + 1)
    ans.append(f'{s} {cnt}')

print('\n'.join(ans), end='')
