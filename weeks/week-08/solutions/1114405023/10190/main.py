"""
10190 - umbrella rain problem

Note:
The provided requirement does not include official sample I/O or enough geometric detail
to fully verify the final formula. This file gives a clean program scaffold that parses input,
defines the data model, and leaves a replaceable solve_core() implementation point.

You can still submit this as a structured template, then fill the math once the official
statement/sample is confirmed.
"""

import sys
from dataclasses import dataclass

@dataclass
class Umbrella:
    x: int
    length: int
    speed: int

def parse(data: str):
    lines = [line.strip() for line in data.strip().splitlines() if line.strip()]
    if not lines:
        return 0, 0, 0, 0, []
    n, w, t, v = map(int, lines[0].split())
    umbrellas = []
    for i in range(1, n + 1):
        x, l, s = map(int, lines[i].split())
        umbrellas.append(Umbrella(x, l, s))
    return n, w, t, v, umbrellas

def solve_core(n: int, w: int, t: int, v: int, umbrellas) -> float:
    """
    Placeholder:
    total rain volume on road = uncovered_area_time_integral * V

    Replace this function with the verified geometry/deduction once you have the
    official samples or complete statement.
    """
    raise NotImplementedError("10190 needs the official sample or full statement to finish exactly.")

def solve(data: str) -> str:
    n, w, t, v, umbrellas = parse(data)
    ans = solve_core(n, w, t, v, umbrellas)
    return f"{ans:.2f}"

if __name__ == "__main__":
    try:
        print(solve(sys.stdin.read()))
    except NotImplementedError as e:
        print(str(e))
