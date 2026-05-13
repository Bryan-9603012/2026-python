import sys

def solve(data: str) -> str:
    tokens = data.split()

    if not tokens:

        return ""
    t = int(tokens[0])
    ans = []
    p = 1

    for _ in range(t):
        s = int(tokens[p])
        d = int(tokens[p + 1])
        p += 2

        if s >= d and ((s + d) & 1) == 0:
            ans.append(f"{(s + d) // 2} {(s - d) // 2}")
        else:
            ans.append("impossible")
    return "\n".join(ans)

def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))

if __name__ == "__main__":

    main()
