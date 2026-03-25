#!/usr/bin/env python3
"""UVA 10057 - A mid-summer night's dream"""
from __future__ import annotations
import sys
from bisect import bisect_left, bisect_right


def analyze(values: list[int]) -> tuple[int, int, int]:
    values.sort()
    n = len(values)
    left_mid = values[(n - 1) // 2]
    right_mid = values[n // 2]
    count = bisect_right(values, right_mid) - bisect_left(values, left_mid)
    possibilities = right_mid - left_mid + 1
    return left_mid, count, possibilities


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    idx = 0
    out = []
    while idx < len(nums):
        n = nums[idx]
        idx += 1
        arr = nums[idx:idx + n]
        idx += n
        a, count, possibilities = analyze(arr)
        out.append(f"{a} {count} {possibilities}")
    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == '__main__':
    main()
