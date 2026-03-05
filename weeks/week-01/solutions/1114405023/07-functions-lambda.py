# 檔案：函數和Lambda表達式練習
# 學習普通函數定義和Lambda匿名函數的用法

# 定義一個普通函數，將輸入值乘以2
def double(x):
    return x * 2

# 使用列表推導式和double函數
values = [1, 2, 3]
result = [double(x) for x in values]

# 定義包含字典的列表
rows = [{'name': 'A', 'score': 90}, {'name': 'B', 'score': 75}]
# 使用sorted()函數和lambda表達式按score鍵排序
rows_stored = sorted(rows, key=lambda r: r['score'])

print(result)  # 輸出: [2, 4, 6]
print(rows_stored)  # 輸出: [{'name': 'B', 'score': 75}, {'name': 'A', 'score': 90}]