nums = [1,2,3]
sum(x*x for x in nums)

s = ('ACME', 50, 123.45)
','.join(str(x) for x in s)

portfolios = [
    {'name': 'AOL', 'shares': 50},{'name': 'YHOO', 'shares': 75}]
min(s['shares'] for s in portfolios)
min(portfolios, key=lambda s: s['shares'])

print(list(x*x for x in nums))
print(list(str(x) for x in s))
print(list(s['shares'] for s in portfolios))