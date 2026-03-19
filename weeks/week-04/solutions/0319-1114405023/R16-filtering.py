# R16-filtering.py
# 示範列表推導、filter 與 itertools.compress 篩選技巧
mylist = [1, 4, -5, 10]
# 推導式篩選正數
[n for n in mylist if n > 0]
pos = [n for n in mylist if n > 0]

values = ['1', '2', '-3', '-', 'N/A']

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

# filter 只留下能轉為整數的值
print(list(filter(is_int, values)))

from itertools import compress
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]
more5 = [n > 5 for n in counts]
# compress 根據布林序列挑選匹配項目
print(list(compress(addresses, more5)))
print(list(compress(addresses, [n > 5 for n in counts])))
print(list(compress(addresses, [n > 0 for n in counts])))
print(list(compress(addresses, [n > 10 for n in counts])))