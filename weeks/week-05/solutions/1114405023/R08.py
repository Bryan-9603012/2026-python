from datetime import datetime,date,timedelta
from calendar import monthrange

def get_month_range(start:date | None = None)->tuple[date,date]:
    if start is None:
        start = date.today().replace(day=1)
    _,days = monthrange(start.year,start.month)
    return start,start + timedelta(days=days)

first,last = get_month_range(date(2012,8,1))
print(first,"~",last - timedelta(days=1))

def date_range(start:datetime,stop:datetime,step:timedelta):
    while start<stop:
        yield start
        start += step

for d in date_range(datetime(2012,9,1),datetime(2012,9,2),timedelta(hours=6)):
    print(d)

text = "2012-09-20"
dt = datetime.strptime(text,"%Y-%m-%d")
print(dt)
print(datetime.strftime(dt,"%A %B %d,%Y"))

def parse_ymd(s:str)->datetime:
    y,m,d = s.split("-")
    return datetime(int(y),int(m),int(d))

print(parse_ymd("2012-09-20"))