# 檔案：變量賦值練習
# 學習基本變量賦值和元組解包

# 單個變量賦值
x = 10
name = "John Doe"

# 多個變量同時賦值（元組賦值）
x, y = 3, 5

# 定義函數返回多個值
def get_point():
    return 4, 9

# 接收函數返回的多個值（解包）
px, py = get_point()

# 輸出結果
print(x)  # 輸出: 10
print(name)  # 輸出: John Doe
print(px, py)  # 輸出: 4 9