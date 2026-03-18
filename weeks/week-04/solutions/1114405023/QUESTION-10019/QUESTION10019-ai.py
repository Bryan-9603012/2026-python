def solve():
    import sys
    # 逐行讀取標準輸入，每行是一組 a b 整數
    for line in sys.stdin:
        # 解析兩個整數 a, b
        a, b = map(int, line.split())
        # 印出絕對差值 |a - b|
        print(abs(a - b))