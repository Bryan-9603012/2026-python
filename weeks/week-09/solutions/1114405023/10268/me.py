import sys

a = list(map(int, sys.stdin.read().split()))
ans = []
for i in range(0, len(a), 2):
    k, n = a[i], a[i + 1]
    if k == 0:
        break
    dp = [0] * (k + 1)
    ok = False
    for m in range(1, 64):
        for e in range(k, 0, -1):
            dp[e] = dp[e] + dp[e - 1] + 1
        if dp[k] >= n:
            ans.append(str(m))
            ok = True
            break
    if not ok:
        ans.append('More than 63 trials needed.')

print('\n'.join(ans), end='')
