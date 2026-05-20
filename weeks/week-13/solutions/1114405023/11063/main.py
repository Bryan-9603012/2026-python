"""
UVA 11063 - RGB to XYZ 色彩轉換
將 RGB 像素轉換為 XYZ 表色系統，並計算平均亮度 Y。
轉換公式：
  X = 0.5149*R + 0.3244*G + 0.1607*B
  Y = 0.2654*R + 0.6704*G + 0.0642*B
  Z = 0.0248*R + 0.1248*G + 0.8504*B
"""

import sys


def rgb_to_xyz(r, g, b):
    """將 RGB 值轉換為 XYZ 值"""
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z


def solve():
    input_data = sys.stdin.read().split()
    idx = 0

    def next_int():
        nonlocal idx
        val = int(input_data[idx])
        idx += 1
        return val

    n = next_int()  # 影像大小 n*n

    total_y = 0.0
    total_pixels = n * n

    # 逐行讀取像素並轉換
    for row in range(n):
        for col in range(n):
            r = next_int()
            g = next_int()
            b = next_int()

            x, y, z = rgb_to_xyz(r, g, b)
            total_y += y

            # 輸出 XYZ，小數點後 4 位四捨五入
            print(f"{x:.4f} {y:.4f} {z:.4f}")

    # 計算並輸出平均亮度
    avg_y = total_y / total_pixels
    print(f"The average of Y is {avg_y:.4f}")


if __name__ == "__main__":
    solve()
