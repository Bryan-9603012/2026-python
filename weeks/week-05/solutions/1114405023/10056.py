#!/usr/bin/env python3
"""UVA 10056 - What is the Probability ?"""
from __future__ import annotations
import sys


def win_probability(n: int, p: float, i: int) -> float:
    if p == 0.0:
        return 0.0
    q = 1.0 - p
    return (q ** (i - 1) * p) / (1.0 - q ** n)


def solve(data: str) -> str:
    parts = data.split()
    if not parts:
        return ""
    t = int(parts[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(parts[idx])
        p = float(parts[idx + 1])
        i = int(parts[idx + 2])
        idx += 3
        out.append(f"{win_probability(n, p, i):.4f}")
    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == '__main__':
    main()
