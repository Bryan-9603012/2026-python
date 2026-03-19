# R20-chainmap.py
# 示範 collections.ChainMap：多個映射組合成一個視圖
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)

# 先在 a 尋找，找不到才到 b
default_x = c['x']
default_z = c['z']
print(default_x)
print(default_z)
