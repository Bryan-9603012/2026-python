import sys

def solve(text):
    # 優化簡化版：DFS 直接剪枝，不先產生全部 permutations。
    a=[x.strip() for x in text.splitlines() if x.strip()]
    i=0; ans=[]; first=True
    while i<len(a):
        n=int(a[i]); i+=1
        bad=[]
        for _ in range(n):
            s=set()
            for x in map(int,a[i].split()):
                if x==0: break
                s.add(x-1)
            bad.append(s); i+=1
        if not first: ans.append('')
        first=False
        used=[0]*n; path=['']*n; pre=None
        def dfs(pos):
            nonlocal pre
            if pos==n:
                cur=''.join(path)
                if pre is None: ans.append(cur)
                else:
                    k=0
                    while k<n and pre[k]==cur[k]: k+=1
                    ans.append(cur[k:])
                pre=cur; return
            for p in range(n):
                if not used[p] and pos not in bad[p]:
                    used[p]=1; path[pos]=chr(65+p); dfs(pos+1); used[p]=0
        dfs(0)
    return '\n'.join(ans)

if __name__=='__main__': print(solve(sys.stdin.read()),end='')
