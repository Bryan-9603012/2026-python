import math
R = 6440.0
try:
    while True:
        s, a, unit = input().split()
        s = float(s)
        a = float(a)
        if unit == "min":
            a /= 60.0
        if a > 180:
            a = 360 - a
        r = R + s
        rad = math.radians(a)
        arc = r * rad
        chord = 2 * r * math.sin(rad / 2)
        print(f"{arc:.6f} {chord:.6f}")
except EOFError:
    pass
