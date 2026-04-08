import sys

def ok(board, chosen, r, c, n, m):
    if board[r][c] != 'P':
        return False
    for dc in (1, 2):
        if c - dc >= 0 and chosen[r][c - dc]:
            return False
        if c + dc < m and chosen[r][c + dc]:
            return False
    for dr in (1, 2):
        if r - dr >= 0 and chosen[r - dr][c]:
            return False
        if r + dr < n and chosen[r + dr][c]:
            return False
    return True

def brute(board):
    n = len(board)
    m = len(board[0])
    chosen = [[False] * m for _ in range(n)]
    best = 0

    def dfs(idx, placed):
        nonlocal best
        if idx == n * m:
            best = max(best, placed)
            return
        if placed + (n * m - idx) <= best:
            return
        r, c = divmod(idx, m)
        dfs(idx + 1, placed)
        if ok(board, chosen, r, c, n, m):
            chosen[r][c] = True
            dfs(idx + 1, placed + 1)
            chosen[r][c] = False

    dfs(0, 0)
    return best

def solve(data: str) -> str:
    parts = data.strip().split()
    if not parts:
        return ""
    n = int(parts[0])
    m = int(parts[1])
    board = parts[2:2 + n]
    return str(brute(board))

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
