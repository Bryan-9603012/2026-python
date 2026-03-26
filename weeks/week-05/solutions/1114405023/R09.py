from datetime import datetime, timedelta
from zoneinfo import ZoneInfo,available_timezones

utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

d = datetime(2012,12,21,9,30,0,tzinfo=central)
print(d)

print(d.astimezone(ZoneInfo("Asia/Taipei")))
print(d.astimezone(taipei))

now_utc = datetime.now(tz = utc)
print(now_utc)

utc_dt = datetime(2013,3,10,7,45,0,tzinfo=utc)
print(utc_dt.astimezone(central))

tw_zones = [z for z in available_timezones()if "Taipei" in z]
print(tw_zones)