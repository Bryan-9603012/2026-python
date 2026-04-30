import csv
import json
import time
import io
import xml.etree.ElementTree as ET
import functools

def read_csv_raw(data: str) -> list:
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall('row')]

def timeit(func):

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'  {func.__name__:<20s} {elapsed:.6f}s')
        return result
    return wrapper

def demo():
    pass
wrapped = timeit(demo)
print('未加 wraps 前：', wrapped.__name__)

def timeit(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'  {func.__name__:<20s} {elapsed:.6f}s')
        return result
    return wrapper
wrapped = timeit(demo)
print('加 wraps 後：  ', wrapped.__name__)
print()
N = 1000
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=['id', 'name', 'score'])
writer.writeheader()
for i in range(N):
    writer.writerow({'id': i, 'name': f'Student{i:04d}', 'score': 60 + i % 40})
CSV_DATA = csv_buf.getvalue()
JSON_DATA = json.dumps([{'id': i, 'name': f'Student{i:04d}', 'score': 60 + i % 40} for i in range(N)])
xml_rows = ''.join((f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>' for i in range(N)))
XML_DATA = f'<data>{xml_rows}</data>'

def timeit_silent(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return (result, time.perf_counter() - start)
    return wrapper
_csv = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml = timeit_silent(read_xml_raw)
RUNS = 5
times = {'CSV': 0.0, 'JSON': 0.0, 'XML': 0.0}
for _ in range(RUNS):
    _, t = _csv(CSV_DATA)
    times['CSV'] += t
    _, t = _json(JSON_DATA)
    times['JSON'] += t
    _, t = _xml(XML_DATA)
    times['XML'] += t
print(f'=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n')
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
base = times['JSON'] / RUNS
for fmt, total in times.items():
    avg = total / RUNS
    print(f'  {fmt:<6} {avg:.6f}s   {avg / base:>8.2f}x')
