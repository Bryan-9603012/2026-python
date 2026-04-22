import sys

lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
out = []
i = 0

while i < len(lines):
    n = int(lines[i])
    i += 1
    ban = []

    for _ in range(n):
        a = list(map(int, lines[i].split()))
        i += 1
        ban.append(set(a[:-1]))

    used = [0] * n
    cur = [''] * n
    prev = [None]
    ans = []

    def dfs(p: int):
        if p == n:
            s = ''.join(cur)
            if prev[0] is None:
                ans.append(s)
            else:
                k = 0
                while k < n and s[k] == prev[0][k]:
                    k += 1
                ans.append(s[k:])
            prev[0] = s
            return

        for x in range(n):
            if not used[x] and (p + 1) not in ban[x]:
                used[x] = 1
                cur[p] = chr(65 + x)
                dfs(p + 1)
                used[x] = 0

    dfs(0)
    out.append('\n'.join(ans))

print('\n\n'.join(out), end='')