import csv
import io
raw = 'Symbol,Price,Date,Time,Change,Volume\nAA,39.48,6/11/2007,9:36am,-0.18,181800\nAIG,71.38,6/11/2007,9:36am,-0.15,195500\nAXP,62.58,6/11/2007,9:36am,-0.46,935000\n'
print('=== csv.reader ===')
f = io.StringIO(raw)
reader = csv.reader(f)
headers = next(reader)
print('標頭：', headers)
for row in reader:
    print(row)
print('\n=== csv.DictReader ===')
f = io.StringIO(raw)
for row in csv.DictReader(f):
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")
print('\n=== csv.writer ===')
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(['Symbol', 'Price', 'Change'])
writer.writerow(['AA', 39.48, -0.18])
writer.writerow(['AIG', 71.38, -0.15])
print(output.getvalue())
print('=== csv.DictWriter ===')
output = io.StringIO()
fieldnames = ['Symbol', 'Price', 'Change']
writer = csv.DictWriter(output, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({'Symbol': 'AA', 'Price': 39.48, 'Change': -0.18})
writer.writerow({'Symbol': 'AIG', 'Price': 71.38, 'Change': -0.15})
print(output.getvalue())
