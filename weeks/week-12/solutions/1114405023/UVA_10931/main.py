import sys


def solve(data: str) -> str:
    out = []
    for token in data.split():
        n = int(token)
        if n == 0:
            break
        binary = bin(n)[2:]
        parity = binary.count('1')
        out.append(f"The parity of {binary} is {parity} (mod 2).")
    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
