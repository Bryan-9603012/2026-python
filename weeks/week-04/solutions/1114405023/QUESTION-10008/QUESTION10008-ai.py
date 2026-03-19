def solve():
    import sys
    input = sys.stdin.readline

    # 第一行輸入 n，代表後面會有 n 行測資
    n = int(input())
    # freq 用來記錄每個字母出現次數
    freq = {}

    for _ in range(n):
        # 去除行首行尾空白，轉成大寫方便統一計數
        line = input().strip().upper()   # ⭐ 重點：strip()
        for ch in line:
            # 只計算英文字母 A-Z，其它符號忽略
            if 'A' <= ch <= 'Z':
                freq[ch] = freq.get(ch, 0) + 1

    # 依次數由大到小；若次數相同則按字母順序排序
    result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # 輸出格式：字母 + 空格 + 次數
    for ch, count in result:
        print(ch, count)