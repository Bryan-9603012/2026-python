import sys
from collections import deque

sys.setrecursionlimit(10**6)
a = list(map(int, sys.stdin.read().split()))
it = iter(a)
n, m = next(it), next(it)
g = [[] for _ in range(n)]
r = [[] for _ in range(n)]
e = []

for _ in range(m):
    u, v = next(it) - 1, next(it) - 1
    g[u].append(v)
    r[v].append(u)
    e.append((u, v))

val = [next(it) for _ in range(n)]
s, p = next(it) - 1, next(it)
bars = [next(it) - 1 for _ in range(p)]

vis = [0] * n
order = []

def dfs(u):
    vis[u] = 1
    for v in g[u]:
        if not vis[v]:
            dfs(v)
    order.append(u)

for i in range(n):
    if not vis[i]:
        dfs(i)

comp = [-1] * n
sumc = []

def rdfs(u, c):
    comp[u] = c
    s0 = val[u]
    for v in r[u]:
        if comp[v] == -1:
            s0 += rdfs(v, c)
    return s0

c = 0
for u in reversed(order):
    if comp[u] == -1:
        sumc.append(rdfs(u, c))
        c += 1

dag = [[] for _ in range(c)]
ind = [0] * c
for u, v in e:
    x, y = comp[u], comp[v]
    if x != y:
        dag[x].append(y)

for i in range(c):
    dag[i] = list(set(dag[i]))
    for v in dag[i]:
        ind[v] += 1

q = deque([i for i in range(c) if ind[i] == 0])
ord2 = []
while q:
    u = q.popleft()
    ord2.append(u)
    for v in dag[u]:
        ind[v] -= 1
        if ind[v] == 0:
            q.append(v)

INF = -10**18
dp = [INF] * c
dp[comp[s]] = sumc[comp[s]]

for u in ord2:
    if dp[u] == INF:
        continue
    for v in dag[u]:
        dp[v] = max(dp[v], dp[u] + sumc[v])

bar = [0] * c
for b in bars:
    bar[comp[b]] = 1

print(max(dp[i] for i in range(c) if bar[i]), end='')
