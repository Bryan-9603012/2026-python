import sys
import math

def min_b_plus_c(a: int) -> int:
    x = a * a + 1
    best = 10**30
    for d in range(1, int(math.isqrt(x)) + 1):
        if x % d == 0:
            e = x // d
            best = min(best, 2 * a + d + e)
    return best

def solve(data: str) -> str:
    a = int(data.strip())
    return str(min_b_plus_c(a))

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
