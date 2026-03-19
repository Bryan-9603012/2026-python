# R17-dict-subset.py
# 使用字典推導式過濾字典資料
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}
# 只留下價值高於200的項目
p1 = {k: v for k, v in prices.items() if v > 200}

tech_names = {'AAPL', 'IBM'}
# 只留下鍵在 tech_names 的項目
p2 = {k: v for k, v in prices.items() if k in tech_names}

print(p1)
print(p2)  