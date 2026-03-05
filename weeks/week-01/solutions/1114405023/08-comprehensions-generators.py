# 檔案：推導式和生成器表達式練習
# 學習列表推導式、字典推導式和生成器表達式

# 定義一個混合正負數的列表
nums = [1, -2, 3, -4]
# 列表推導式：篩選出所有正數
positives = [n for n in nums if n > 0]

# 定義包含元組的列表
pairs = [('a', 1), ('b', 2)]
# 字典推導式：將元組列表轉換為字典
lookup = {k: v for k, v in pairs}

# 生成器表達式：計算所有元素平方和（不產生中間列表）
squares_sum = sum(n * n for n in nums)

print(positives)  # 輸出: [1, 3]
print(lookup)  # 輸出: {'a': 1, 'b': 2}
print(squares_sum)  # 輸出: 30（1 + 4 + 9 + 16）