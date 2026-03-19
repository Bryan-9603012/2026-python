# U05.py
# 範例：使用 heapq 實作優先佇列，tuple 順序比較優先
import heapq

class Item:
    def __init__(self, name):
        self.name = name

pq = []
idx = 0
# 使用負數 priority 轉成 max-heap 形式，避免同優先度時比較 Item 物件
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1

print(Item('a').name, Item('b').name)  # 優先佇列裡的 item 仍是 Item 實例