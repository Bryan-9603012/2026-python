#!/usr/bin/env python3
"""UVA 10041 - Vito's Family"""
from __future__ import annotations
import sys


def min_total_distance(addresses: list[int]) -> int:
    addresses = sorted(addresses)
    median = addresses[len(addresses) // 2]
    return sum(abs(x - median) for x in addresses)


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""
    t = nums[0]
    idx = 1
    out = []
    for _ in range(t):
        r = nums[idx]
        idx += 1
        arr = nums[idx:idx + r]
        idx += r
        out.append(str(min_total_distance(arr)))
    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == '__main__':
    main()
