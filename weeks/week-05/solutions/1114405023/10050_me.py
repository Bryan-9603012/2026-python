import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    p = int(sys.stdin.readline())

    hartals = [0] * (n + 1)

    for _ in range(p):
        h = int(sys.stdin.readline())
        day = h
        while day <= n:
            if day % 7 != 6 and day % 7 != 0:
                hartals[day] = 1
            day += h

    print(sum(hartals))