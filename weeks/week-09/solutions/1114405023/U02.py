# Understand（理解）- itertools 工具函數
# 從 itertools 匯入常用工具：
# islice：對迭代器做切片
# dropwhile：前面符合條件的元素全部跳過
# takewhile：前面符合條件的元素全部取出
# chain：把多個可迭代物件串接起來
# permutations：排列
# combinations：組合
from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


# 建立一個無限遞增的產生器，從 n 開始一直加 1
def count(n):
    i = n
    while True:
        yield i
        i += 1


# 建立從 0 開始的無限序列
c = count(0)

# 取出索引 5 到 9 的元素（不包含 10）
# 等同於切片 [5:10]
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")

# 準備測試資料
nums = [1, 3, 5, 2, 4, 6]

# 從前面開始檢查，當條件 x < 5 成立時就持續跳過
# 一旦遇到第一個不符合條件的元素，就停止跳過，後面全部保留
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")

# 從前面開始檢查，當條件 x < 5 成立時就持續取出
# 一旦遇到第一個不符合條件的元素，就停止取值
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")

# 三個不同串列
a = [1, 2]
b = [3, 4]
c = [5]

# 將多個可迭代物件接成一個連續序列
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")

# 排列測試資料
items = ["a", "b", "c"]

# 列出 items 所有可能的全排列
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

# 列出 items 中取 2 個元素的所有排列
# 排列會考慮順序，所以 ('a', 'b') 和 ('b', 'a') 視為不同
print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")

# 列出 items 中取 2 個元素的所有組合
# 組合不考慮順序，所以 ('a', 'b') 和 ('b', 'a') 視為相同
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")

# 假設可用字元
chars = ["A", "B", "1"]

# 用排列產生所有 2 位數密碼（不重複使用字元）
print("2位數密碼:")
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")

# 匯入可重複組合工具
from itertools import combinations_with_replacement

# combinations_with_replacement 表示可重複選取元素
# 但它屬於「組合」，不考慮順序
# 例如 AB 和 BA 只會出現一種
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")