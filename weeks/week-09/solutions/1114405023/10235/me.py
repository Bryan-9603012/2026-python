import sys

MOD = 1000000007
a = list(map(int, sys.stdin.read().split()))
t = a[0]
p = 1
res = []
for case in range(1, t + 1):
    n, m = a[p], a[p + 1]
    p += 2
    g = []
    for _ in range(n):
        g.append(a[p:p + m])
        p += m

    dp = [0] * (1 << (m + 1))
    dp[0] = 1
    mask = (1 << (m + 1)) - 1

    for i in range(n):
        nxt = [0] * (1 << (m + 1))
        for s, v in enumerate(dp):
            if v:
                nxt[(s << 1) & mask] = v
        dp = nxt

        for j in range(1, m + 1):
            nxt = [0] * (1 << (m + 1))
            x, y = 1 << (j - 1), 1 << j
            for s, v in enumerate(dp):
                if not v:
                    continue
                l, u = (s >> (j - 1)) & 1, (s >> j) & 1
                if g[i][j - 1] == 0:
                    if l == 0 and u == 0:
                        nxt[s] = (nxt[s] + v) % MOD
                else:
                    nxt[s ^ x ^ y] = (nxt[s ^ x ^ y] + v) % MOD
                    if l != u:
                        nxt[s] = (nxt[s] + v) % MOD
            dp = nxt

    res.append(f'Case {case}: {dp[0]}')

print('\n'.join(res), end='')
