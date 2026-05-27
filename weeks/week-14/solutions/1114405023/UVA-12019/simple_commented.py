import sys

# 題目給定的 Doomsday 基準表；在原 UVA / ZeroJudge 題目中這些日期是 Monday
doomsday = [10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 第一行是測試資料筆數
t = int(sys.stdin.readline())

for _ in range(t):
    # 讀取月份與日期
    month, day = map(int, sys.stdin.readline().split())

    # 和該月 Doomsday 相差幾天，再對 7 取餘數
    print(weekdays[(day - doomsday[month - 1]) % 7])
