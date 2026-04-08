import sys

def solve(data: str) -> str:
    data = data.strip().split()
    if not data:
        return ""
    n = int(data[0])
    smaller_before = [0] * (n + 1)
    for i in range(2, n + 1):
        smaller_before[i] = int(data[i - 1])

    available = list(range(1, n + 1))
    ans = [0] * (n + 1)
    for pos in range(n, 0, -1):
        idx = smaller_before[pos]
        ans[pos] = available.pop(idx)
    return "\n".join(map(str, ans[1:]))

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
