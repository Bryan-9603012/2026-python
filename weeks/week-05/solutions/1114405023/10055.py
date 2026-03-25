#!/usr/bin/env python3
"""QUESTION-10055 custom problem: function monotonicity toggles and range queries."""
from __future__ import annotations
import sys


class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def prefix_sum(self, idx: int) -> int:
        total = 0
        while idx > 0:
            total += self.bit[idx]
            idx -= idx & -idx
        return total

    def range_sum(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""
    n, q = nums[0], nums[1]
    idx = 2
    bit = FenwickTree(n)
    state = [0] * (n + 1)  # 0 increasing, 1 decreasing
    out = []

    for _ in range(q):
        v = nums[idx]
        idx += 1
        if v == 1:
            i = nums[idx]
            idx += 1
            if state[i] == 0:
                state[i] = 1
                bit.add(i, 1)
            else:
                state[i] = 0
                bit.add(i, -1)
        else:
            l = nums[idx]
            r = nums[idx + 1]
            idx += 2
            decreasing_count = bit.range_sum(l, r)
            out.append('1' if decreasing_count % 2 else '0')

    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == '__main__':
    main()
