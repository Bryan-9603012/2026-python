p = (4,5)
x, y = p

data = ["ACME", 50, 91.1,(2012, 12, 21)]
name, shares, price, date = data
name, shares, price, (year, month, day) = data

_, shares, price, _ = data
print(shares, price)
print(p)
print(x, y)
print(name, shares, price, data)
print(year, month, day)
print(_)