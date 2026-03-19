# U10.py
# 範例：zip 生成器一旦遍歷完即耗盡
prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())

print(min(z))  # 先消耗 zip 生成器取得最小項
print(list(z))  # 之後已無資料，輸出 []
