# U09.py
# 示範為何 groupby 需先排序：未排序時同一 key 會被視為不同群組

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 未排序時，groupby 會在第一個 '07/02/2012' 之後結束該組
for k, g in groupby(rows, key=itemgetter('date')):
    print(k, list(g))

rows.sort(key=itemgetter('date'))
# 排序後，同一天的元素才會合併成一組
for k, g in groupby(rows, key=itemgetter('date')):
    print(k, list(g))

print(rows)