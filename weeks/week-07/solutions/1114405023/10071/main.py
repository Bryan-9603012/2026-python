import sys
from collections import Counter

def solve(data: str) -> str:
    parts = data.strip().split()
    if not parts:
        return ""
    n = int(parts[0])
    s = list(map(int, parts[1:1 + n]))

    triple = Counter()
    for a in s:
        for b in s:
            ab = a + b
            for c in s:
                triple[ab + c] += 1

    pair = Counter()
    for d in s:
        for e in s:
            pair[d + e] += 1

    ans = 0
    for t_sum, t_cnt in triple.items():
        for f in s:
            ans += t_cnt * pair.get(f - t_sum, 0)
    return str(ans)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
