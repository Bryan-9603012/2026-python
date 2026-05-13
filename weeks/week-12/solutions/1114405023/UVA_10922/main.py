import sys


def digit_sum(s: str) -> int:
    total = 0
    for ch in s:
        total += ord(ch) - ord('0')
    return total


def nine_degree(s: str) -> int:
    total = digit_sum(s)
    degree = 1

    while total > 9:
        total = digit_sum(str(total))
        degree += 1

    return degree if total == 9 else 0


def solve(data: str) -> str:
    out = []
    for s in data.split():
        if s == "0":
            break
        degree = nine_degree(s)
        if degree:
            out.append(f"{s} is a multiple of 9 and has 9-degree {degree}.")
        else:
            out.append(f"{s} is not a multiple of 9.")
    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
