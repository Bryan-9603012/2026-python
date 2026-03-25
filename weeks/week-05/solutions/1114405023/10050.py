#!/usr/bin/env python3
"""UVA 10050 - Hartals"""
from __future__ import annotations
import sys


def lost_working_days(n: int, hartals: list[int]) -> int:
    days_lost = set()
    for h in hartals:
        for day in range(h, n + 1, h):
            weekday = day % 7
            if weekday in (6, 0):  # Friday or Saturday
                continue
            days_lost.add(day)
    return len(days_lost)


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""
    t = nums[0]
    idx = 1
    out = []
    for _ in range(t):
        n = nums[idx]
        idx += 1
        p = nums[idx + 0]
        idx += 1
        hartals = nums[idx:idx + p]
        idx += p
        out.append(str(lost_working_days(n, hartals)))
    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == '__main__':
    main()
