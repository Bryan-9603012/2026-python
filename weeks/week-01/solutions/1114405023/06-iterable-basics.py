# 檔案：可迭代對象基礎練習
# 學習可迭代對象和迭代器的概念

# 定義一個列表
items = [1, 2, 3]

# 定義一個函數，它接受可迭代對象並遍歷其元素
def consume(it):
    for x in it:
        pass  # 只是遍歷，不做任何操作

# 測試consume函數：列表是可迭代的
consume(items)
# 字符串也是可迭代的
consume('abc')

# 使用zip()函數將兩個列表的對應元素配對
z = zip([1, 2], [3, 4])
# 將迭代器轉換為列表（注意：迭代器只能遍歷一次）
first = list(z)
# 第二次轉換時，迭代器已經耗盡，結果為空列表
second = list(z)

print(first)  # 輸出: [(1, 3), (2, 4)]
print(second)  # 輸出: []（迭代器已耗盡）