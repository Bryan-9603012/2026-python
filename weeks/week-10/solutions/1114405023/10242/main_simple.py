import sys
sys.setrecursionlimit(1_000_000)

def solve(text):
    # 優化簡化版：SCC 壓縮成 DAG，再做最大路徑 DP。
    a=list(map(int,text.split()))
    if not a: return ''
    i=0; n,m=a[i],a[i+1]; i+=2
    g=[[] for _ in range(n)]; rg=[[] for _ in range(n)]
    for _ in range(m):
        u,v=a[i]-1,a[i+1]-1; i+=2; g[u].append(v); rg[v].append(u)
    cash=a[i:i+n]; i+=n
    s,p=a[i]-1,a[i+1]; i+=2; pubs=[x-1 for x in a[i:i+p]]
    seen=[0]*n; order=[]
    def dfs(u):
        seen[u]=1
        for v in g[u]:
            if not seen[v]: dfs(v)
        order.append(u)
    for u in range(n):
        if not seen[u]: dfs(u)
    comp=[-1]*n; val=[]
    def rdfs(u,c):
        comp[u]=c; val[c]+=cash[u]
        for v in rg[u]:
            if comp[v]<0: rdfs(v,c)
    for u in reversed(order):
        if comp[u]<0:
            val.append(0); rdfs(u,len(val)-1)
    c=len(val); dag=[set() for _ in range(c)]
    for u in range(n):
        for v in g[u]:
            if comp[u]!=comp[v]: dag[comp[u]].add(comp[v])
    target={comp[x] for x in pubs}; memo={}
    def best(u):
        if u in memo: return memo[u]
        res=val[u] if u in target else -10**30
        for v in dag[u]:
            b=best(v)
            if b>=0: res=max(res,val[u]+b)
        memo[u]=res; return res
    return str(best(comp[s]))

if __name__=='__main__': print(solve(sys.stdin.read()),end='')
