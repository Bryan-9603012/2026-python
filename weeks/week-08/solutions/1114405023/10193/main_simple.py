import math
a = int(input().strip())
x = a * a + 1
ans = 10**18
for d in range(1, int(math.isqrt(x)) + 1):
    if x % d == 0:
        e = x // d
        ans = min(ans, 2 * a + d + e)
print(ans)
