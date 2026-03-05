# 檔案：排序和比較練習
# 學習元組比較、sorted函數和min函數的使用

# 定義兩個元組
a = (1, 2)
b = (1, 3)
# 比較元組：元組按元素逐個比較
result = a < b  # 第一個元素相同，比較第二個元素：2 < 3

# 定義包含字典的列表
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
# 使用sorted()函數按uid鍵對列表進行排序
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# 使用min()函數找到uid最小的字典
smallest = min(rows, key=lambda r: r['uid'])

print(result)  # 輸出: True
print(rows_sorted)  # 輸出: [{'uid': 1}, {'uid': 2}, {'uid': 3}]
print(smallest)  # 輸出: {'uid': 1}