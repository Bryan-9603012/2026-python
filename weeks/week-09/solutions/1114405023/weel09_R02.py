# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# 使用 Path 物件來組合路徑，比字串拼接更安全、可讀性更好
# "/" 在 pathlib 中代表路徑串接，不是數學除法
base = Path("weeks") / "week-09"

print(base)         # 輸出完整路徑：weeks/week-09（Windows 會自動顯示成反斜線）
print(base.name)    # 取得路徑最後一層名稱：week-09
print(base.parent)  # 取得上一層路徑：weeks
print(base.suffix)  # 取得副檔名，這裡是資料夾名稱所以沒有副檔名，結果為 ''

# 建立一個檔案路徑物件
f = Path("hello.txt")

# stem：檔名本體（不含副檔名）
# suffix：副檔名
print(f.stem, f.suffix)  # hello .txt

# 相容舊寫法：os.path.join
# 這是舊式但仍很常見的路徑組合方式
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
# 建立 hello.txt 的路徑物件
p = Path("hello.txt")

print(p.exists())   # 檢查路徑是否存在
print(p.is_file())  # 檢查是否為檔案
print(p.is_dir())   # 檢查是否為資料夾

# 建立一個不存在的檔案路徑
missing = Path("no_such_file.txt")

# 若檔案不存在，就不要去讀它，避免發生錯誤
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
# "." 代表目前所在資料夾
here = Path(".")

# 只列出目前資料夾第一層內容
# os.listdir() 回傳名稱字串，不會附帶完整路徑資訊
for name in os.listdir(here):
    print("listdir:", name)

# 只找目前資料夾底下副檔名為 .py 的檔案
# glob("*.py") 只搜尋當前層，不會進入子資料夾
for p in here.glob("*.py"):
    print("glob:", p)

# 遞迴搜尋上層資料夾（..）及其所有子資料夾中的 .py 檔案
# rglob("*.py") 會一路往下搜尋所有符合條件的檔案
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用：只印出找到的第一個 .py 檔案