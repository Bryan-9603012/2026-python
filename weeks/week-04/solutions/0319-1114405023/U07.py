# U07.py
# 範例：OrderedDict 維持插入順序（python3.7 後普通 dict 亦保留）
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

print(d)