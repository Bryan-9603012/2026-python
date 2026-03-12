from itertools import groupby
from operator import itemgetter

rows = [{'date':'07/01/2012','address':'...'},
        {'date':'07/02/2012','address':'...'},]
rows.sort(key=itemgetter('date'))
print(rows)

for date, items in groupby(rows, key=itemgetter('date')):
    for i in items:
        pass

print(date)