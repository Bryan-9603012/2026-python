from collections import ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)

c['x']
c['z']

print(c['x'])
print(c['z'])
