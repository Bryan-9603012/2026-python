import sys
from math import isqrt

for line in sys.stdin:
    # 讀取閉區間 [a, b]
    a, b = map(int, line.split())

    # 0 0 代表結束
    if a == 0 and b == 0:
        break

    # <= b 的完全平方數有 isqrt(b) 個
    # < a 的完全平方數有 isqrt(a - 1) 個
    print(isqrt(b) - isqrt(a - 1))
