"""UVA 11332 - Mirror Visibility (簡化版)"""
import sys
import math

def norm(a):
    a = a % (2 * math.pi)
    if a < 0:
        a += 2 * math.pi
    return a

def get_intervals(sx, sy, ex, ey):
    a1 = norm(math.atan2(sy, sx))
    a2 = norm(math.atan2(ey, ex))
    lo, hi = min(a1, a2), max(a1, a2)
    if hi - lo > math.pi:
        return [(hi, 2*math.pi), (0, lo)]
    return [(lo, hi)]

def min_dist(sx, sy, ex, ey):
    return min(math.sqrt(sx*sx+sy*sy), math.sqrt(ex*ex+ey*ey))

def merge(ivs):
    if not ivs:
        return []
    ivs.sort()
    m = [ivs[0]]
    for s, e in ivs[1:]:
        if s <= m[-1][1]:
            m[-1] = (m[-1][0], max(m[-1][1], e))
        else:
            m.append((s, e))
    return m

def covered(new, cov):
    for ns, ne in new:
        cur = ns
        ok = False
        for cs, ce in cov:
            if cs > cur:
                break
            if cs <= cur <= ce:
                cur = max(cur, ce)
                if cur >= ne:
                    ok = True
                    break
        if not ok:
            return False
    return True

def solve():
    data = sys.stdin.read().split()
    idx = 0
    results = []
    while idx < len(data):
        n = int(data[idx]); idx += 1
        if n == 0:
            break
        mirrors = []
        for i in range(n):
            sx = int(data[idx]); idx += 1
            sy = int(data[idx]); idx += 1
            ex = int(data[idx]); idx += 1
            ey = int(data[idx]); idx += 1
            ivs = get_intervals(sx, sy, ex, ey)
            d = min_dist(sx, sy, ex, ey)
            mirrors.append((d, i, ivs))
        mirrors.sort()
        vis = [False] * n
        cov = []
        for d, i, ivs in mirrors:
            if not covered(ivs, cov):
                vis[i] = True
                cov = merge(cov + ivs)
        results.append(''.join('1' if v else '0' for v in vis))
    print('\n'.join(results))

if __name__ == "__main__":
    solve()
