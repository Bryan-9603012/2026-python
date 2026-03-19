# U04.py
# 範例：heapq 是小頂堆，h[0] 永遠是最小值
import heapq

nums = [5, 1, 9, 2]
h = nums[:]
heapq.heapify(h)
# h[0] 永遠是最小值（這是 heap 的核心性質）
m = heapq.heappop(h)  # 每次 pop 取得最小值

print(m)  # 1