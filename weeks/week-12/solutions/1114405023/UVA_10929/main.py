import sys


def is_multiple_of_11(num: str) -> bool:
    odd_sum = 0
    even_sum = 0

    for i, ch in enumerate(num):
        digit = ord(ch) - ord('0')
        if i % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    return abs(odd_sum - even_sum) % 11 == 0


def solve(data: str) -> str:
    out = []
    for num in data.split():
        if num == "0":
            break
        if is_multiple_of_11(num):
            out.append(f"{num} is a multiple of 11.")
        else:
            out.append(f"{num} is not a multiple of 11.")
    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
