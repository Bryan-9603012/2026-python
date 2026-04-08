import sys
import re

# 七段顯示器 bitmask
# 每個數字對應一個 7-bit 狀態，用來判斷能不能透過移動木棒轉換
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
    # 把像是 "12-3+4" 這種字串算出值
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
    # 必須且只能有一個等號
    if expr.count('=') != 1:
        return False

    left, right = expr.split('=')

    # 左右兩邊都必須是合法的加減整數式
    if not re.fullmatch(r'[+-]?\d+(?:[+-]\d+)*', left):
        return False
    if not re.fullmatch(r'[+-]?\d+(?:[+-]\d+)*', right):
        return False

    # 等式左右值相等才算成立
    return parse_side(left) == parse_side(right)


def solve(data: str) -> str:
    if not data:
        return ""

    # 題目輸入以 # 結尾，後面可能有垃圾字元，所以只取 # 前面
    sharp = data.find('#')
    expr = data[:sharp].strip() if sharp != -1 else data.strip()
    suffix = '#' if sharp != -1 else ''

    chars = list(expr)

    # 只允許移動「數字」的木棒，所以只處理數字位置
    pos = [i for i, ch in enumerate(chars) if ch.isdigit()]

    # 枚舉木棒移動前後的所有可能
    for i in pos:
        for j in pos:
            if i == j:
                # 同一個數字內部重排：總木棒數不變
                for a in DIGITS:
                    if a == chars[i]:
                        continue

                    # 木棒數要一樣，且剛好只移動一根（bit 差 2）
                    if SEG[a].bit_count() != SEG[chars[i]].bit_count():
                        continue
                    if (SEG[a] ^ SEG[chars[i]]).bit_count() != 2:
                        continue

                    out = chars[:]
                    out[i] = a
                    if valid_equation(''.join(out)):
                        return ''.join(out) + suffix
            else:
                # 不同數字之間移動：i 少一根，j 多一根
                for a in DIGITS:
                    if a == chars[i]:
                        continue

                    # i 失去一根木棒
                    if SEG[a].bit_count() + 1 != SEG[chars[i]].bit_count():
                        continue
                    if (SEG[a] ^ SEG[chars[i]]).bit_count() != 1:
                        continue
                    if (SEG[a] & ~SEG[chars[i]]) != 0:
                        continue

                    for b in DIGITS:
                        if b == chars[j]:
                            continue

                        # j 增加一根木棒
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
