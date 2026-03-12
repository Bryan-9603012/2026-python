prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55,'FB': 10.75}

min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))

min(prices, key=lambda k: prices[k])

print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))
print(sorted(prices, key=lambda k: prices[k]))
print(sorted(prices, key=lambda k: prices[k], reverse=True))