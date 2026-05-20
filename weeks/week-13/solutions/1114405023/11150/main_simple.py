"""UVA 11150 - Frog Crossing (簡化版)"""
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    stones = set()
    for _ in range(M):
        stones.add(int(data[idx])); idx += 1

    if S == T:
        print(sum(1 for p in stones if p % S == 0))
        return

    sorted_stones = sorted(stones)
    comp = [0]
    for i in range(len(sorted_stones)):
        gap = sorted_stones[i] - (sorted_stones[i-1] if i > 0 else 0)
        if gap > 90:
            gap = 90
        comp.append(comp[-1] + gap)
    fg = L - sorted_stones[-1]
    if fg > 90:
        fg = 90
    cL = comp[-1] + fg
    cStones = set(comp[1:-1])

    INF = float('inf')
    dp = [INF] * (cL + T + 1)
    dp[0] = 0
    for i in range(1, cL + T + 1):
        for j in range(S, T + 1):
            if i - j >= 0 and dp[i-j] != INF:
                dp[i] = min(dp[i], dp[i-j])
        if i in cStones:
            dp[i] += 1
    print(min(dp[cL:cL+T+1]))

if __name__ == "__main__":
    solve()
