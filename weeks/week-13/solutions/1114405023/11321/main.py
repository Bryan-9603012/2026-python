"""
UVA 11321 - 陷阱放置 (Trap Placement)
在 N*M 的網格上依序放置陷阱，每次檢查放置後是否會封死所有從左到右的路徑。
若不會封死則放置，否則不放。
使用 BFS 檢查連通性。
"""

import sys
from collections import deque


def has_path(N, M, traps):
    """檢查從左側(y=0)到右側(y=M-1)是否仍有路徑"""
    # 起點：所有左側未被封鎖的格子
    visited = [[False] * M for _ in range(N)]
    queue = deque()

    for x in range(N):
        if (x, 0) not in traps:
            visited[x][0] = True
            queue.append((x, 0))

    if not queue:
        return False

    # BFS
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        if y == M - 1:  # 到達右側
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and (nx, ny) not in traps:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return False


def solve():
    input_data = sys.stdin.read().split()
    idx = 0

    def next_int():
        nonlocal idx
        val = int(input_data[idx])
        idx += 1
        return val

    N = next_int()  # 縱軸（列數）
    M = next_int()  # 橫軸（行數）
    T = next_int()  # 陷阱數量

    traps = set()  # 已放置的陷阱

    for _ in range(T):
        x = next_int()
        y = next_int()

        # 嘗試放置陷阱
        traps.add((x, y))

        if has_path(N, M, traps):
            # 仍有路徑，保留陷阱
            print("<(_ _)>")
        else:
            # 封死了，移除陷阱
            traps.remove((x, y))
            print(">_<")


if __name__ == "__main__":
    solve()
