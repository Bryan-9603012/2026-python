import sys
from collections import defaultdict
MOD=1_000_000_007

def solve(text):
    # 優化簡化版：輪廓線 DP，不做暴力擺蛇。
    data=list(map(int,text.split()))
    if not data: return ''
    p=1; out=[]
    for case in range(1,data[0]+1):
        n,m=data[p],data[p+1]; p+=2
        g=[data[p+i*m:p+(i+1)*m] for i in range(n)]; p+=n*m
        dp={(0,0):1}  # (上方連線 mask, 左方連線)
        for r in range(n):
            for c in range(m):
                nd=defaultdict(int)
                for (mask,left),cnt in dp.items():
                    up=(mask>>c)&1; base=mask & ~(1<<c)
                    if g[r][c]==0:
                        if up==0 and left==0:
                            nd[(base,0)]=(nd[(base,0)]+cnt)%MOD
                        continue
                    for right in (0,1):
                        if right and c==m-1: continue
                        for down in (0,1):
                            if down and r==n-1: continue
                            if up+left+right+down==2:
                                nm=base | (down<<c)
                                nl=right if c+1<m else 0
                                nd[(nm,nl)]=(nd[(nm,nl)]+cnt)%MOD
                dp=nd
        out.append(f'Case {case}: {dp.get((0,0),0)%MOD}')
    return '\n'.join(out)

if __name__=='__main__': print(solve(sys.stdin.read()),end='')
