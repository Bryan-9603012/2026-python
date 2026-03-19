# R18-namedtuple.py
# 示範 collections.namedtuple 使用 (不可變結構型別)
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', joined='2012-10-19')
# 以屬性存取
print(sub.addr)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
# _replace 產生新 tuple，舊 tuple 不變
s = s._replace(shares=75)

print(s)
print(s._asdict())
