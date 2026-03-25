import sys

t = int(sys.stdin.readline())

for _ in range(t):
    nums = list(map(int, sys.stdin.readline().split()))
    r = nums[0]
    streets = nums[1:]

    streets.sort()
    mid = streets[r // 2]

    total = 0
    for x in streets:
        total += abs(x - mid)

    print(total)