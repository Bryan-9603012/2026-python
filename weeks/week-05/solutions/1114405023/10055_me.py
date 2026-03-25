import sys

n, q = map(int, sys.stdin.readline().split())

flip = [0] * (n + 1)

for _ in range(q):
    data = list(map(int, sys.stdin.readline().split()))

    if data[0] == 1:
        x = data[1]
        flip[x] ^= 1
    else:
        l = data[1]
        r = data[2]

        cnt = 0
        for i in range(l, r + 1):
            cnt += flip[i]

        if cnt % 2 == 0:
            print(0)
        else:
            print(1)