import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, p, i = sys.stdin.readline().split()
    n = int(n)
    p = float(p)
    i = int(i)

    if p == 0:
        print("0.0000")
    else:
        ans = ((1 - p) ** (i - 1) * p) / (1 - (1 - p) ** n)
        print(f"{ans:.4f}")