# 檔案：索引和切片練習
# 學習如何使用索引和切片訪問序列中的元素

# 定義字符串
text = 'abcdefg'
# 使用索引訪問第一個字符（索引從0開始）
first = text[0]
# 使用切片訪問從索引2到5（不包括5）的子串
mid = text[2:5]

# 定義列表
num = [10, 20, 30, 40, 50]
# 使用負索引和切片訪問最後兩個元素
last_two = num[-2:]

# 輸出結果
print(first)  # 輸出: a
print(mid)  # 輸出: cde
print(last_two)  # 輸出: [40, 50]