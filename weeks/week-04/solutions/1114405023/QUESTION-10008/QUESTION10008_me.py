def solve():
    import sys
    input = sys.stdin.readline

    n = int(input())
    freq = {}

    for _ in range(n):
        line = input().strip().upper()   # ⭐ 重點：strip()
        for ch in line:
            if 'A' <= ch <= 'Z':
                freq[ch] = freq.get(ch, 0) + 1

    result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    for ch, count in result:
        print(ch, count)