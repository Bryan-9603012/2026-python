def solve():
    import sys
    input = sys.stdin.readline

    # 測資組數 M
    M = int(input())
    for case_index in range(M):
        # 每組測資之間有空行（題目輸入格式）
        input()
        # N: 硬幣數，K: 天平實驗次數
        N, K = map(int, input().split())

        # possible 保存目前仍有可能為假幣的編號（1~N）
        # 先假設每顆都有可能，後面逐步排除
        possible = set(range(1, N + 1))

        for _ in range(K):
            data = list(map(int, input().split()))
            result = input().strip()

            p = data[0]
            # 左盤硬幣編號
            left = set(data[1:1 + p])
            # 右盤硬幣編號
            right = set(data[1 + p:1 + 2 * p])

            if result == "=":
                # 公平：左右盤所有硬幣必為真幣，剔除這些
                possible -= (left | right)
            else:
                # 不平衡：假幣必在此次天平上（左或右）
                involved = left | right
                possible &= involved

        # 若最終只有一顆硬幣可能為假，輸出
        if len(possible) == 1:
            print(possible.pop())
        else:
            # 無法唯一確定則輸出 0
            print(0)

        # 每組輸出後都要空一行（與題目輸出格式一致）
        if case_index != M - 1:
            print()