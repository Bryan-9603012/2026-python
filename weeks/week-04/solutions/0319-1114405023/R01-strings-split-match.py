# R01-strings-split-match.py
# 示範字串拆分及通配符匹配
# 主要用到 re.split 與 fnmatch

import re
from fnmatch import fnmatch, fnmatchcase

line = "asdf fjdk afed, fjek,asdf, foo"
# re.split 依照正規表達式切割字串，連續空白或逗號都可被拆分
print(re.split(r'[,\s]+', line))

# 此 pattern 可能有筆誤，正常情況應該是 r'(?:,|\s)+'
# 以問號加冒號為非捕獲群組，避免擷取關聯結果
print(re.split(r"(?:,|\s)+", line))

filename = "spam.txt"
# fnmatch 用通配符來判斷是否符合模式
print(fnmatch(filename, "*.txt"))  # True
print(fnmatch(filename, "file:*"))  # False

filename_list = ["Makefile", "foo.c", "spam.py", "spam.h", "spam.h"]
# endswith 可傳 tuple 進行多重後綴判斷
print([name for name in filename_list if name.endswith((".c", ".h"))])

print(fnmatch("food.txt", "*.txt"))
# [] 中的 0-9 代表字元範圍
print(fnmatch("Dat45.csv", "Dat[0-9]*"))

# fnmatch 預設大小寫敏感，下面會回傳 False
print(fnmatch("food.txt", ".TXT"))

addresses = [
    "5412 N CLARK ST",
    "1060 W ADDISON ST",
    "1039 W GRAND AV"
]
# 只有以 ST 結尾的地址符合
print([a for a in addresses if fnmatch(a, "* ST")])
