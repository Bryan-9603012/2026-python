import sys


def ok(board, chosen, r, c, n, m):
    # 只能放在平原 P 上
    if board[r][c] != 'P':
        return False

    # 檢查同一列左右 1 格、2 格是否已有炮兵
    for dc in (1, 2):
        if c - dc >= 0 and chosen[r][c - dc]:
            return False
        if c + dc < m and chosen[r][c + dc]:
            return False

    # 檢查同一欄上下 1 格、2 格是否已有炮兵
    for dr in (1, 2):
        if r - dr >= 0 and chosen[r - dr][c]:
            return False
        if r + dr < n and chosen[r + dr][c]:
            return False

    return True


def brute(board):
    n = len(board)
    m = len(board[0])

    # chosen[r][c] = 目前這格是否已放炮兵
    chosen = [[False] * m for _ in range(n)]
    best = 0

    def dfs(idx, placed):
        nonlocal best

        # 所有格子都考慮完，更新最佳答案
        if idx == n * m:
            best = max(best, placed)
            return

        # 簡單剪枝：就算剩下格子全部都能放，也不會超過 best
        if placed + (n * m - idx) <= best:
            return

        # 把一維索引轉回 (r, c)
        r, c = divmod(idx, m)

        # 選擇 1：這格不放炮兵
        dfs(idx + 1, placed)

        # 選擇 2：這格可以放時，嘗試放炮兵
        if ok(board, chosen, r, c, n, m):
            chosen[r][c] = True
            dfs(idx + 1, placed + 1)
            chosen[r][c] = False

    dfs(0, 0)
    return best


def solve(data: str) -> str:
    # 讀入 n, m 與地圖
    parts = data.strip().split()
    if not parts:
        return ""
    n = int(parts[0])
    m = int(parts[1])
    board = parts[2:2 + n]

    # 簡單版直接暴力搜尋最大值
    return str(brute(board))


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
