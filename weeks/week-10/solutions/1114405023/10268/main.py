import sys

def solve(text):
    ans=[]
    for line in text.splitlines():
        if not line.strip(): continue
        k,n=map(int,line.split())
        if k==0: break
        dp=[0]*(k+1); found=None
        for t in range(1,64):
            for e in range(k,0,-1):
                dp[e]=min(1<<63, dp[e]+dp[e-1]+1)
            if dp[k]>=n:
                found=t; break
        ans.append(str(found) if found is not None else 'More than 63 trials needed.')
    return '\n'.join(ans)

if __name__=='__main__': print(solve(sys.stdin.read()),end='')
