# R19-generator-aggregate.py
# 示範 generator expression 與彙整函式
nums = [1, 2, 3]
# generator expression 可直接傳給 sum，不會建立中間列表
print(sum(x*x for x in nums))

s = ('ACME', 50, 123.45)
# join 需要字串，使用生成式轉換
print(','.join(str(x) for x in s))

portfolios = [
    {'name': 'AOL', 'shares': 50},
    {'name': 'YHOO', 'shares': 75}
]
# 直接對 generator 計算最小值
eprint_val = min(p['shares'] for p in portfolios)
print(eprint_val)
# min 加上 key 找出 shares 最小的字典
print(min(portfolios, key=lambda p: p['shares']))

print(list(x*x for x in nums))
print(list(str(x) for x in s))
print(list(p['shares'] for p in portfolios))