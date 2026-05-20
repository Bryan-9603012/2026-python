"""
UVA 11005 - Cheapest Base
給定每個字元(0-9, A-Z)的印刷成本，找出將數字印在不同進位制下成本最低的進位制。
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

    T = next_int()  # 測試資料組數

    for case_num in range(1, T + 1):
        # 讀取 36 個字元的成本 (0-9, A-Z)
        costs = []
        for _ in range(36):
            costs.append(next_int())

        Q = next_int()  # 查詢數量
        queries = []
        for _ in range(Q):
            queries.append(next_int())

        if case_num > 1:
            print()  # 測試資料之間空一行

        print(f"Case {case_num}:")

        for n in queries:
            if n == 0:
                # 0 在任何進位制下都是 "0"
                min_cost = costs[0]
                cheapest_bases = []
                for base in range(2, 37):
                    if costs[0] == min_cost:
                        cheapest_bases.append(base)
                print(f"Cheapest base(s) for number {n}: {' '.join(map(str, cheapest_bases))}")
                continue

            # 對每個進位制 2~36 計算成本
            base_costs = {}
            for base in range(2, 37):
                temp = n
                total_cost = 0
                while temp > 0:
                    digit = temp % base
                    total_cost += costs[digit]
                    temp //= base
                base_costs[base] = total_cost

            # 找出最低成本
            min_cost = min(base_costs.values())
            cheapest_bases = sorted([b for b, c in base_costs.items() if c == min_cost])

            print(f"Cheapest base(s) for number {n}: {' '.join(map(str, cheapest_bases))}")


if __name__ == "__main__":
    solve()
