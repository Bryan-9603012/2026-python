# 檔案：基本容器類型練習
# 學習Python的四種基本容器：列表、元組、集合、字典

# 列表（可修改）- 用方括號
number = [1, 2, 3]
# 元組（不可修改）- 用括號
point = (4, 5)
# 集合（不重複的元素集合）- 用大括號
unique = {1, 2, 3}
# 字典（鍵值對）- 用大括號
prices = {'AAPL': 150.0, 'MSFT': 320.5}

# 向列表添加元素
number.append(4)
# 使用索引訪問元組中的元素
first = point[0]
# 使用鍵訪問字典中的值
prices['AAPL']

# 输出结果
print(number)  # 輸出: [1, 2, 3, 4]
print(first)  # 輸出: 4
print(prices['AAPL'])  # 輸出: 150.0