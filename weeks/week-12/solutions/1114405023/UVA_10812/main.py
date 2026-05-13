import sys


def solve(data: str) -> str:
    lines = data.strip().split()
    if not lines:
        return ""

    t = int(lines[0])
    idx = 1
    out = []

    for _ in range(t):
        s = int(lines[idx])
        d = int(lines[idx + 1])
        idx += 2

        high = (s + d) // 2
        low = (s - d) // 2

        if s < d or (s + d) % 2 != 0 or low < 0:
            out.append("impossible")
        else:
            out.append(f"{high} {low}")

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
