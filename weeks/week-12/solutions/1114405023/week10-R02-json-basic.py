import json
data = {'name': 'Alice', 'age': 30, 'scores': [95, 87, 92]}
s = json.dumps(data)
print(type(s), s)
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)
obj = json.loads(s)
print(type(obj), obj['name'])
with open('/tmp/data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
with open('/tmp/data.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)
print(loaded)
print(json.dumps([1, True, None, 'hello']))
record = {'城市': '澎湖', '人口': 100000}
print(json.dumps(record, ensure_ascii=False))
print(json.dumps(record, ensure_ascii=True))
