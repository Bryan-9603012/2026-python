# U08.py
# 範例：min 函式與 zip 配合使用來取得最小值與對應鍵
prices = {'A': 2.0, 'B': 1.0}

print(min(prices))            # 回傳 key 的最小值（字母序）, 結果 'A'
print(min(prices.values()))   # 回傳最小 value, 結果 1.0

# zip 產生 (value, key)，讓 min 根據 value 比較
print(min(zip(prices.values(), prices.keys())))