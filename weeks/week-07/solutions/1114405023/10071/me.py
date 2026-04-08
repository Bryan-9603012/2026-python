import sys

def solve(data: str) -> str:
    parts = data.strip().split()
    if not parts:
        return ""
    n = int(parts[0])
    s = list(map(int, parts[1:1 + n]))

    ans = 0
    for a in s:
        for b in s:
            for c in s:
                for d in s:
                    for e in s:
                        for f in s:
                            if a + b + c + d + e == f:
                                ans += 1
    return str(ans)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
