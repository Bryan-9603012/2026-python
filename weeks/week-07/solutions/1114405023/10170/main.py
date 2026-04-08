import sys

def people_on_day(s: int, d: int) -> int:
    low, high = s, s
    def total(n: int) -> int:
        return n * (n + 1) // 2 - (s - 1) * s // 2
    while total(high) < d:
        high *= 2
    while low < high:
        mid = (low + high) // 2
        if total(mid) >= d:
            high = mid
        else:
            low = mid + 1
    return low

def solve(data: str) -> str:
    ans = []
    for line in data.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        s, d = map(int, line.split())
        ans.append(str(people_on_day(s, d)))
    return "\n".join(ans)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
