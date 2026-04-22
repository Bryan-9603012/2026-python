import sys

MOD = 1_000_000_007

def solve_case(n: int, m: int, grid: list[list[int]]) -> int:
    dp = [0] * (1 << (m + 1))
    dp[0] = 1
    mask = (1 << (m + 1)) - 1

    for i in range(n):
        shifted = [0] * (1 << (m + 1))
        for s, v in enumerate(dp):
            if v:
                shifted[(s << 1) & mask] = v
        dp = shifted

        for j in range(1, m + 1):
            ndp = [0] * (1 << (m + 1))
            x = 1 << (j - 1)
            y = 1 << j
            for s, v in enumerate(dp):
                if not v:
                    continue
                left = 1 if s & x else 0
                up = 1 if s & y else 0
                if grid[i][j - 1] == 0:
                    if left == 0 and up == 0:
                        ndp[s] = (ndp[s] + v) % MOD
                else:
                    ndp[s ^ x ^ y] = (ndp[s ^ x ^ y] + v) % MOD
                    if left != up:
                        ndp[s] = (ndp[s] + v) % MOD
            dp = ndp
    return dp[0]

def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    t = nums[0]
    idx = 1
    out = []
    for case in range(1, t + 1):
        n, m = nums[idx], nums[idx + 1]
        idx += 2
        grid = []
        for _ in range(n):
            grid.append(nums[idx:idx + m])
            idx += m
        out.append(f'Case {case}: {solve_case(n, m, grid)}')
    return '\n'.join(out)

if __name__ == '__main__':
    print(solve(sys.stdin.read()), end='')
