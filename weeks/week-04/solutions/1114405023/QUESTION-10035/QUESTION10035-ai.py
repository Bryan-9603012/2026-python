def solve():
    # 持續讀取測資，每一組為一行兩個數字，0 0 表示結束
    while True:
        a, b = input().split()
        if a == '0' and b == '0':
            break

        # 反轉字串方便從個位數開始做逐位相加
        a = a[::-1]
        b = b[::-1]

        carry = 0   # 是否有進位
        count = 0   # 累積進位次數

        # 最長位數為迴圈次數
        for i in range(max(len(a), len(b))):
            x = int(a[i]) if i < len(a) else 0
            y = int(b[i]) if i < len(b) else 0

            # 檢查本位是否產生進位
            if x + y + carry >= 10:
                carry = 1
                count += 1
            else:
                carry = 0

        # 根據進位數輸出對應結果文字
        if count == 0:
            print("No carry operation.")
        elif count == 1:
            print("1 carry operation.")
        else:
            print(f"{count} carry operations.")