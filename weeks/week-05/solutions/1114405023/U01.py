# R09. 時區操作（3.16）
# Python 3.9 之後，官方推薦使用 zoneinfo 來處理時區，
# 它是標準函式庫的一部分，可用來取代過去常用的 pytz。

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

# 建立三個時區物件：
# UTC：世界協調時間，常作為系統內部統一儲存時間的基準
# America/Chicago：美國中部時間
# Asia/Taipei：台北時間
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 建立一個「帶有時區資訊」的 datetime 物件
# 這裡表示：2012/12/21 上午 9:30，時區是 America/Chicago
# tzinfo=central 代表這不是單純的日期時間，而是「有時區的時間」
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)

# 印出 d
# 結果中的 -06:00 表示這個時間比 UTC 慢 6 小時
# 也就是 UTC = 本地時間 + 6 小時
print(d)  # 2012-12-21 09:30:00-06:00

# astimezone(...) 用來把同一個「時間點」轉換成其他時區表示方式
# 注意：這不是改變事件發生時間，而是換一個地區的時間格式來看它

# 轉換成印度時間 Asia/Kolkata
# 印度時間是 UTC+05:30
# 所以芝加哥時間 2012-12-21 09:30:00-06:00
# 換算後會變成印度時間 2012-12-21 21:00:00+05:30
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30

# 轉換成台北時間 Asia/Taipei
# 台北時間是 UTC+08:00
# 所以同一個時間點換算後會變成 2012-12-21 23:30:00+08:00
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 取得現在的 UTC 時間
# datetime.now(tz=utc) 會直接回傳「帶時區資訊」的目前 UTC 時間
# 這樣比先取得本地時間再轉 UTC 更清楚也更安全
now_utc = datetime.now(tz=utc)
print(now_utc)

# 最佳實踐：
# 在系統內部儲存、計算、比對時間時，盡量統一使用 UTC
# 等到要顯示給不同地區的使用者時，再轉換成對方的本地時區

# 建立一個 UTC 時間：2013/03/10 07:45:00 UTC
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)

# 把 UTC 時間轉換成 Chicago 時間
# 這一天剛好接近美國日光節約時間（DST）切換日期，
# 所以這類操作若用有時區資訊的 datetime 會比較可靠
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# 查詢系統中所有可用的時區名稱
# available_timezones() 會回傳一個包含所有時區字串的集合（set）

# 這裡用串列生成式篩選出名稱中包含 "Taipei" 的時區
# 結果通常只會有 ['Asia/Taipei']
tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']