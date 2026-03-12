prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}
p1 = {k:v for k, v in prices.items() if v > 200}

tech_names = {'AAPL', 'IBM'}
p2 = {k:v for k, v in prices.items() if k in tech_names}

print(p1)
print(p2)  