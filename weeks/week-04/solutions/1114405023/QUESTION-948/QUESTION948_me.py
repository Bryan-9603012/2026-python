def solve():
    import sys
    input = sys.stdin.readline

    M = int(input())
    for case_index in range(M):
        input()
        N, K = map(int, input().split())

        possible = set(range(1, N + 1))

        for _ in range(K):
            data = list(map(int, input().split()))
            result = input().strip()

            p = data[0]
            left = set(data[1:1 + p])
            right = set(data[1 + p:1 + 2 * p])

            if result == "=":
                possible -= (left | right)
            else:
                involved = left | right
                possible &= involved
        if len(possible) == 1:
            print(possible.pop())
        else:
            print(0)
        if case_index != M - 1:
            print()