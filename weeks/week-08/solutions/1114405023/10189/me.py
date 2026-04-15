case_no = 1
first = True
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    g = [input().strip() for _ in range(n)]
    a = [["0"] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if g[i][j] == "*":
                a[i][j] = "*"
            else:
                s = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and g[ni][nj] == "*":
                            s += 1
                a[i][j] = str(s)
    if not first:
        print()
    first = False
    print(f"Field #{case_no}:")
    for row in a:
        print("".join(row))
    case_no += 1
