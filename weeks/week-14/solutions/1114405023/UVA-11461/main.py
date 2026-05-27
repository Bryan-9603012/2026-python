import sys
from math import isqrt

def count_squares(a, b):
    return isqrt(b) - isqrt(a - 1)

def solve(data):
    nums = list(map(int, data.split()))
    out = []
    for i in range(0, len(nums), 2):
        a, b = nums[i], nums[i + 1]
        if a == 0 and b == 0:
            break
        out.append(str(count_squares(a, b)))
    return "\n".join(out)

print(solve(sys.stdin.read()))
