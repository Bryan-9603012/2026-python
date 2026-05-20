"""
UVA 11150 - 青蛙過河 (Frog Crossing)
青蛙從 0 跳到 L，每次跳 S~T 距離，橋上有 M 個石子。
求最少踩到的石子數。
使用路徑壓縮 + 動態規劃。
"""

import sys


def solve():
    input_data = sys.stdin.read().split()
    idx = 0

    def next_int():
        nonlocal idx
        val = int(input_data[idx])
        idx += 1
        return val

    L = next_int()  # 橋的長度
    S = next_int()  # 最小跳躍距離
    T = next_int()  # 最大跳躍距離
    M = next_int()  # 石子數量

    stones = set()
    for _ in range(M):
        stones.add(next_int())

    # 特殊情況：S == T，青蛙每次跳固定距離
    if S == T:
        count = 0
        for pos in stones:
            if pos % S == 0:
                count += 1
        print(count)
        return

    # 路徑壓縮：將石子排序，壓縮過大的間隙
    sorted_stones = sorted(stones)
    compressed = [0]  # 起點

    for i in range(len(sorted_stones)):
        gap = sorted_stones[i] - (sorted_stones[i - 1] if i > 0 else 0)
        # 壓縮間隙：最大保留 90（因為 T <= 10，90 足夠）
        if gap > 90:
            gap = 90
        compressed.append(compressed[-1] + gap)

    # 終點壓縮
    final_gap = L - sorted_stones[-1]
    if final_gap > 90:
        final_gap = 90
    compressed_L = compressed[-1] + final_gap

    # 建立壓縮後的石子位置集合
    compressed_stones = set(compressed[1:-1])  # 排除起點和終點

    # DP：dp[i] = 到達位置 i 最少踩到的石子數
    INF = float('inf')
    max_pos = compressed_L + T  # 可能跳過終點
    dp = [INF] * (max_pos + 1)
    dp[0] = 0

    for i in range(1, max_pos + 1):
        for jump in range(S, T + 1):
            if i - jump >= 0 and dp[i - jump] != INF:
                dp[i] = min(dp[i], dp[i - jump])
        # 如果位置 i 有石子，踩到石子數 +1
        if i in compressed_stones:
            dp[i] += 1

    # 答案：跳到或跳過終點的最小值
    answer = min(dp[compressed_L:compressed_L + T + 1])
    print(answer)


if __name__ == "__main__":
    solve()
