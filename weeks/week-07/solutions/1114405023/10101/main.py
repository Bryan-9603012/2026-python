import sys

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

SAME = {d: [] for d in DIGITS}
LOSE = {d: [] for d in DIGITS}
GAIN = {d: [] for d in DIGITS}

for a in DIGITS:
    ma = SEG[a]
    for b in DIGITS:
        mb = SEG[b]
        diff = ma ^ mb
        if a == b:
            continue
        # same digit: move one segment inside the digit
        if ma.bit_count() == mb.bit_count() and diff.bit_count() == 2:
            if (ma & diff).bit_count() == 1 and (mb & diff).bit_count() == 1:
                SAME[a].append(b)
        # source digit loses one segment
        if ma.bit_count() == mb.bit_count() + 1 and (mb & ~ma) == 0 and diff.bit_count() == 1:
            LOSE[a].append(b)
        # target digit gains one segment
        if mb.bit_count() == ma.bit_count() + 1 and (ma & ~mb) == 0 and diff.bit_count() == 1:
            GAIN[a].append(b)

def parse_expression(expr: str):
    eq = expr.index('=')
    digit_info = {}
    terms = []

    for side_idx, (l, r) in enumerate(((0, eq), (eq + 1, len(expr)))):
        side_sign = 1 if side_idx == 0 else -1
        i = l
        while i < r:
            sign = 1
            if expr[i] == '+':
                sign = 1
                i += 1
            elif expr[i] == '-':
                sign = -1
                i += 1

            start = i
            while i < r and expr[i].isdigit():
                i += 1
            end = i
            num = expr[start:end]
            coeff = side_sign * sign
            value = int(num)
            term_idx = len(terms)
            terms.append({
                'start': start,
                'end': end,
                'coeff': coeff,
                'value': value,
            })
            p = 1
            for pos in range(end - 1, start - 1, -1):
                digit_info[pos] = (term_idx, p, int(expr[pos]))
                p *= 10

    diff0 = sum(t['coeff'] * t['value'] for t in terms)
    return terms, digit_info, diff0

def solve(data: str) -> str:
    if not data:
        return ""
    raw = data
    sharp = raw.find('#')
    if sharp == -1:
        expr = raw.strip()
        suffix = ''
    else:
        expr = raw[:sharp]
        suffix = '#'

    expr = expr.strip()
    if not expr:
        return "No"

    terms, digit_info, diff0 = parse_expression(expr)
    chars = list(expr)
    digit_positions = [i for i, ch in enumerate(chars) if ch.isdigit()]

    def delta_at(pos: int, new_digit: str) -> int:
        term_idx, place, old_digit = digit_info[pos]
        coeff = terms[term_idx]['coeff']
        return coeff * (int(new_digit) - old_digit) * place

    # 1) move inside the same digit
    for i in digit_positions:
        old = chars[i]
        for nd in SAME[old]:
            if diff0 + delta_at(i, nd) == 0:
                out = chars[:]
                out[i] = nd
                return ''.join(out) + suffix

    # 2) move from one digit to another digit
    for i in digit_positions:
        old_i = chars[i]
        if not LOSE[old_i]:
            continue
        for j in digit_positions:
            if i == j:
                continue
            old_j = chars[j]
            if not GAIN[old_j]:
                continue
            for di in LOSE[old_i]:
                d1 = delta_at(i, di)
                for dj in GAIN[old_j]:
                    if diff0 + d1 + delta_at(j, dj) == 0:
                        out = chars[:]
                        out[i] = di
                        out[j] = dj
                        return ''.join(out) + suffix

    return "No"

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
