def solve():
    import sys

    # 讀取標準輸入每一行作為一個測資
    for line in sys.stdin:
        # 將每一行切割為整數列表
        data = list(map(int, line.split()))
        # 第一個數字為 n，代表數列長度
        n = data[0]
        # 剩下的數字為實際數列內容
        arr = data[1:]

        # 若只有一個數，必定為 Jolly
        if n == 1:
            print("Jolly")
            continue

        # 差值集合，儲存每對相鄰元素的絕對差
        diff = set()

        for i in range(1, n):
            d = abs(arr[i] - arr[i-1])
            diff.add(d)

        # Jolly 的條件：差值集合恰好包含 1 到 n-1
        if diff == set(range(1, n)):
            print("Jolly")
        else:
            print("Not jolly")