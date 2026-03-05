# 檔案：導入、類和異常處理練習
# 學習module導入、類定義、異常處理的基本用法

# 從collections模塊導入deque類
from collections import deque

# 創建一個最大長度為2的雙端隊列
q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)  # 當個數超過maxlen時，最左邊的元素會被移除

# 定義一個User類
class User:
    # 構造函數
    def __init__(self, user_id):
        self.user_id = user_id

# 創建User類的實例
u = User(42)
# 訪問類的屬性
uid = u.user_id

# 定義一個函數，嘗試將值轉換為整數
def is_int(val):
    try:
        int(val)  # 嘗試轉換
        return True
    except ValueError:  # 捕獲異常
        return False  # 如果轉換失敗，返回False

print(q)  # 輸出: deque([2, 3], maxlen=2)
print(uid)  # 輸出: 42
print(is_int('a'))  # 輸出: False（字符串'a'無法轉換為整數）
