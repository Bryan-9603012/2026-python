from datetime import datetime,timedelta

a = timedelta(days=2,hours=6)
b = timedelta(hours=4.5)
c=a+b
print(c.days)
print(c.total_seconds()/3600)

dt = datetime(2012,9,23)
print(dt + timedelta(days=10))

d1,d2 = datetime(2012,9,23),datetime(2012,12,21)
print((d2-d1).days)

print((datetime(2012,3,1)-datetime(2012,2,28)).days)
print((datetime(2013,3,1)-datetime(2013,2,28)).days)

WEEKDAYS=[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

def get_previous_byday(dayname:str,start:datetime | None = None)->datetime:
    if start is None:
        start = datetime.today()
    day_num = start.weekday()
    target = WEEKDAYS.index(dayname)
    days_ago = (7+day_num-target)%7 or 7
    return start - timedelta(days=days_ago)

base = datetime(2012,8,28)
print(get_previous_byday("Monday",base))
print(get_previous_byday("Friday",base))


