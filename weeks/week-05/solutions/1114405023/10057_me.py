import sys
from bisect import bisect_left, bisect_right

nums = list(map(int, sys.stdin.read().split()))

n = nums[0]
arr = nums[1:]

arr.sort()

if n % 2 == 1:
    a = arr[n // 2]
    count = arr.count(a)
    print(a, count, 1)
else:
    left = arr[n // 2 - 1]
    right = arr[n // 2]

    a = left
    count = bisect_right(arr, right) - bisect_left(arr, left)
    ways = right - left + 1

    print(a, count, ways)