import sys
from math import isqrt

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    print(isqrt(b) - isqrt(a - 1))
