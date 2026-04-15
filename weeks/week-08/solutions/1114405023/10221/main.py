import sys
import math

R = 6440.0

def solve_line(s: float, a: float, unit: str) -> str:
    r = R + s
    if unit == "min":
        a /= 60.0
    if a > 180.0:
        a = 360.0 - a
    rad = math.radians(a)
    arc = r * rad
    chord = 2.0 * r * math.sin(rad / 2.0)
    return f"{arc:.6f} {chord:.6f}"

def solve(data: str) -> str:
    out = []
    for line in data.strip().splitlines():
        if not line.strip():
            continue
        s, a, unit = line.split()
        out.append(solve_line(float(s), float(a), unit))
    return "\n".join(out)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
