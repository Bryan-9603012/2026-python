# 檔案：for循環練習
# 學習使用for循環遍歷列表

# 定義一個列表
items = [2, 4, 6]

# 使用for循環計算列表中所有元素的和
total = 0
for x in items:
    total += x  # 將每個元素加到total

# 使用for循環和append()創建新列表
squares = []
for x in items:
    squares.append(x * x)  # 將每個元素的平方添加到列表

# 輸出結果
print(total)  # 輸出: 12（2+4+6）
print(squares)  # 輸出: [4, 16, 36]