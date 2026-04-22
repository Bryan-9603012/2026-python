import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    it = iter(nums)
    n, m = next(it), next(it)

    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = next(it) - 1, next(it) - 1
        g[u].append(v)
        rg[v].append(u)
        edges.append((u, v))

    money = [next(it) for _ in range(n)]
    start, p = next(it) - 1, next(it)
    bars = [next(it) - 1 for _ in range(p)]

    order = []
    seen = [False] * n

    def dfs1(u: int) -> None:
        seen[u] = True
        for v in g[u]:
            if not seen[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not seen[i]:
            dfs1(i)

    comp = [-1] * n
    comp_sum = []

    def dfs2(u: int, cid: int) -> int:
        comp[u] = cid
        total = money[u]
        for v in rg[u]:
            if comp[v] == -1:
                total += dfs2(v, cid)
        return total

    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            comp_sum.append(dfs2(u, cid))
            cid += 1

    dag = [[] for _ in range(cid)]
    indeg = [0] * cid
    for u, v in edges:
        cu, cv = comp[u], comp[v]
        if cu != cv:
            dag[cu].append(cv)

    for u in range(cid):
        dag[u] = list(set(dag[u]))
        for v in dag[u]:
            indeg[v] += 1

    q = deque(i for i in range(cid) if indeg[i] == 0)
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in dag[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    NEG = -10**18
    dp = [NEG] * cid
    scc_start = comp[start]
    dp[scc_start] = comp_sum[scc_start]

    for u in topo:
        if dp[u] == NEG:
            continue
        for v in dag[u]:
            dp[v] = max(dp[v], dp[u] + comp_sum[v])

    is_bar = [False] * cid
    for b in bars:
        is_bar[comp[b]] = True

    return str(max(dp[i] for i in range(cid) if is_bar[i]))

if __name__ == '__main__':
    print(solve(sys.stdin.read()), end='')
