import sys

def solve(data: str) -> str:
    lines=[x.strip() for x in data.splitlines() if x.strip()]
    i=0; out=[]; first=True
    while i<len(lines):
        n=int(lines[i]); i+=1
        bad=[set() for _ in range(n)]
        for person in range(n):
            for x in map(int,lines[i].split()):
                if x==0: break
                bad[person].add(x-1)
            i+=1
        if not first: out.append('')
        first=False
        used=[False]*n; path=['']*n; prev=None
        def dfs(pos):
            nonlocal prev
            if pos==n:
                cur=''.join(path)
                if prev is None: out.append(cur)
                else:
                    k=0
                    while k<n and prev[k]==cur[k]: k+=1
                    out.append(cur[k:])
                prev=cur; return
            for p in range(n):
                if not used[p] and pos not in bad[p]:
                    used[p]=True; path[pos]=chr(65+p)
                    dfs(pos+1)
                    used[p]=False
        dfs(0)
    return '\n'.join(out)

if __name__=='__main__': print(solve(sys.stdin.read()),end='')
