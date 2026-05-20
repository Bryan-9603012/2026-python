"""UVA 11005 - Cheapest Base (簡化版)"""
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    for case in range(1, T + 1):
        costs = [int(data[idx + i]) for i in range(36)]
        idx += 36
        Q = int(data[idx]); idx += 1
        if case > 1:
            print()
        print(f"Case {case}:")
        for _ in range(Q):
            n = int(data[idx]); idx += 1
            if n == 0:
                c = costs[0]
                bases = [b for b in range(2, 37) if costs[0] == c]
                print(f"Cheapest base(s) for number {n}: {' '.join(map(str, bases))}")
                continue
            bc = {}
            for base in range(2, 37):
                t, s = n, 0
                while t > 0:
                    s += costs[t % base]
                    t //= base
                bc[base] = s
            mn = min(bc.values())
            bases = sorted(b for b, c in bc.items() if c == mn)
            print(f"Cheapest base(s) for number {n}: {' '.join(map(str, bases))}")

if __name__ == "__main__":
    solve()
