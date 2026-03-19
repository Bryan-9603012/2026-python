def main():
    import sys

    lines = [line.rstrip("\n") for line in sys.stdin]

    if not lines:
        return

    max_len = max(len(line) for line in lines)

    for col in range(max_len):
        rotated = []

        for row in range(len(lines) - 1, -1, -1):
            if col < len(lines[row]):
                rotated.append(lines[row][col])
            else:
                rotated.append(" ")

        print("".join(rotated).rstrip())


if __name__ == "__main__":
    main()