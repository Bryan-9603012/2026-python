import sys

def solve(data: str) -> str:
    out = []
    for line in data.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        s, d = map(int, line.split())
        cur = s
        days = 0
        while True:
            days += cur
            if days >= d:
                out.append(str(cur))
                break
            cur += 1
    return "\n".join(out)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
