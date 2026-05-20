"""UVA 11321 - Trap Placement (簡化版)"""
import sys
from collections import deque

def has_path(N, M, traps):
    visited = [[False]*M for _ in range(N)]
    q = deque()
    for x in range(N):
        if (x,0) not in traps:
            visited[x][0] = True
            q.append((x,0))
    if not q:
        return False
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        x, y = q.popleft()
        if y == M-1:
            return True
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and (nx,ny) not in traps:
                visited[nx][ny] = True
                q.append((nx,ny))
    return False

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    traps = set()
    for _ in range(T):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        traps.add((x,y))
        if has_path(N, M, traps):
            print("<(_ _)>")
        else:
            traps.remove((x,y))
            print(">_<")

if __name__ == "__main__":
    solve()
