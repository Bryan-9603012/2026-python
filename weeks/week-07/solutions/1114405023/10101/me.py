import sys
import re

SEG = {
    '0': 0b1111110,
    '1': 0b0110000,
    '2': 0b1101101,
    '3': 0b1111001,
    '4': 0b0110011,
    '5': 0b1011011,
    '6': 0b1011111,
    '7': 0b1110000,
    '8': 0b1111111,
    '9': 0b1111011,
}
DIGITS = '0123456789'

def parse_side(side: str) -> int:
    total = 0
    i = 0
    n = len(side)
    while i < n:
        sign = 1
        if side[i] == '+':
            i += 1
        elif side[i] == '-':
            sign = -1
            i += 1
        j = i
        while j < n and side[j].isdigit():
            j += 1
        total += sign * int(side[i:j])
        i = j
    return total

def valid_equation(expr: str) -> bool:
    if expr.count('=') != 1:
        return False
    left, right = expr.split('=')
    if not re.fullmatch(r'[+-]?\d+(?:[+-]\d+)*', left):
        return False
    if not re.fullmatch(r'[+-]?\d+(?:[+-]\d+)*', right):
        return False
    return parse_side(left) == parse_side(right)

def solve(data: str) -> str:
    if not data:
        return ""
    sharp = data.find('#')
    expr = data[:sharp].strip() if sharp != -1 else data.strip()
    suffix = '#' if sharp != -1 else ''

    chars = list(expr)
    pos = [i for i, ch in enumerate(chars) if ch.isdigit()]

    for i in pos:
        for j in pos:
            if i == j:
                for a in DIGITS:
                    if a == chars[i]:
                        continue
                    # one moved inside same digit
                    if SEG[a].bit_count() != SEG[chars[i]].bit_count():
                        continue
                    if (SEG[a] ^ SEG[chars[i]]).bit_count() != 2:
                        continue
                    out = chars[:]
                    out[i] = a
                    if valid_equation(''.join(out)):
                        return ''.join(out) + suffix
            else:
                for a in DIGITS:
                    if a == chars[i]:
                        continue
                    # i loses one segment
                    if SEG[a].bit_count() + 1 != SEG[chars[i]].bit_count():
                        continue
                    if (SEG[a] ^ SEG[chars[i]]).bit_count() != 1:
                        continue
                    if (SEG[a] & ~SEG[chars[i]]) != 0:
                        continue
                    for b in DIGITS:
                        if b == chars[j]:
                            continue
                        # j gains one segment
                        if SEG[b].bit_count() != SEG[chars[j]].bit_count() + 1:
                            continue
                        if (SEG[b] ^ SEG[chars[j]]).bit_count() != 1:
                            continue
                        if (SEG[chars[j]] & ~SEG[b]) != 0:
                            continue
                        out = chars[:]
                        out[i] = a
                        out[j] = b
                        if valid_equation(''.join(out)):
                            return ''.join(out) + suffix
    return "No"

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
