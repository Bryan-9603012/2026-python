import sys

def min_trials(k: int, n: int) -> str:
    dp = [0] * (k + 1)
    for moves in range(1, 64):
        for eggs in range(k, 0, -1):
            dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
        if dp[k] >= n:
            return str(moves)
    return 'More than 63 trials needed.'

def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    out = []
    for i in range(0, len(nums), 2):
        k, n = nums[i], nums[i + 1]
        if k == 0:
            break
        out.append(min_trials(k, n))
    return '\n'.join(out)

if __name__ == '__main__':
    print(solve(sys.stdin.read()), end='')
