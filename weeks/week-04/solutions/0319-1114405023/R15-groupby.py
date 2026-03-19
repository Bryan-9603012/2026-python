# R15-groupby.py
# 示範 itertools.groupby 使用方式：資料須先排序，才能分組
from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/01/2012', 'address': '...'},
    {'date': '07/02/2012', 'address': '...'},
]
# 先按 date 排序
rows.sort(key=itemgetter('date'))
print(rows)

# groupby 依據 date 分組，items 是迭代器，迭代後無法重用
for date, items in groupby(rows, key=itemgetter('date')):
    for i in items:
        # 這裡可處理該日期對應的每一筆資料
        pass

# 迴圈完成後，date 仍保留最後一個群組的鍵
print(date)