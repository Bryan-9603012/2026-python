# U06.py
# 範例：使用 dict 與 defaultdict 聚合相同鍵值
from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 一般 dict 需要先判斷是否存在鍵
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)

# defaultdict 遇到不存在的鍵會自動建立預設容器
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)

print(d)
print(d2)