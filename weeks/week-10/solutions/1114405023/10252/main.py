import sys

def calc(arr):
    arr.sort(); n=len(arr)
    l,r=arr[(n-1)//2],arr[n//2]
    return sum(abs(x-l) for x in arr), r-l+1

def solve(text):
    a=list(map(int,text.split()))
    if not a: return ''
    i=1; out=[]
    for _ in range(a[0]):
        n=a[i]; i+=1; xs=[]; ys=[]
        for _ in range(n):
            xs.append(a[i]); ys.append(a[i+1]); i+=2
        sx,cx=calc(xs); sy,cy=calc(ys)
        out.append(f'{sx+sy} {cx*cy}')
    return '\n'.join(out)

if __name__=='__main__': print(solve(sys.stdin.read()),end='')
