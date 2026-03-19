# U03.py
# 範例：deque(maxlen=n) 會保留固定長度，超出時自動丟棄最舊項目
from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)

# 最後只保留最新三筆資料
print(q)  # 結果: deque([3, 4, 5])