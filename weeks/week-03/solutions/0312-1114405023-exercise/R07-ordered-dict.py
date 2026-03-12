from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1; d['bar'] = 2;
json.dumps(d)

print(d)
print(json.dumps(d))