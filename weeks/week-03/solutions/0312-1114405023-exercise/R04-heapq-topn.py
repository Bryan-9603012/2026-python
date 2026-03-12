import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(3, nums)  # [42, 37, 23]
heapq.nsmallest(3, nums)  # [-4, 1, 2]

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22}
    ]
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])  # [{'name': 'AAPL', 'shares': 50, 'price': 543.22}]
heap = list(nums)
heapq.heapify(heap)
heapq.heappop(heap)  # -4

print(heap)  # [1, 2, 2, 23, 7, -4, 18, 23, 42, 37]
print(heap[0])  # 1
print(heap[1])  # 2
print(heap[2])  # 2
print(heap[3])  # 23
print(heap[4])  # 7
print(heap[5])  # -4
print(heap[6])  # 18
print(heap[7])  # 23  
print(heap[8])  # 42
print(heap[9])  # 37