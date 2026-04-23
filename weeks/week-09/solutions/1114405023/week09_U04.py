# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用

import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 可以在記憶體中建立一個像檔案一樣的物件
# 你可以對它使用 print(..., file=...)、read()、write()、seek() 等操作
# 它不會真的寫到硬碟，很適合測試、暫存文字資料
buf = io.StringIO()

# 把文字像寫入檔案一樣寫進 buf
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# 取出目前整個緩衝區中的文字內容
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 也能像讀檔一樣使用：
# 因為前面寫入後游標已經在最後面，所以要先 seek(0) 回到開頭
buf.seek(0)

# enumerate(buf, 1) 代表從第 1 行開始編號
# 這裡直接逐行讀取 StringIO，就像讀真實檔案一樣
for i, line in enumerate(buf, 1):
    print(i, line.rstrip())  # rstrip() 去掉每行尾端換行

# 為什麼 StringIO 很有用？
# 因為很多函式庫只要求你提供「像檔案的物件」（file-like object）
# 不一定真的要是硬碟上的檔案。
# 只要有相似的方法（如 read、write），就能被當成檔案使用。
# 這就是所謂的鴨子型別（duck typing）：
# 「看起來像鴨子、走起來像鴨子、叫起來像鴨子，那它就可以當鴨子用。」

# 例如 csv 模組就可以直接寫到 StringIO，而不必真的建立 .csv 檔
import csv

mem = io.StringIO()
writer = csv.writer(mem)

# 寫入一列標題
writer.writerow(["name", "score"])

# 寫入一列資料
writer.writerow(["alice", 90])

print("---CSV in memory---")
print(mem.getvalue())  # 直接取出記憶體中的 CSV 內容

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 先建立一個多行文字檔
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：讀取 poem.txt
# 1. 跳過空白行
# 2. 幫每一行加上行號
# 3. 寫到新檔 poem_numbered.txt
dst = Path("poem_numbered.txt")

# 同時開啟輸入檔與輸出檔
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    
    n = 0  # 記錄有效行數（不算空行）

    # 逐行讀取檔案：一次只載入一行，適合大檔案
    for line in fin:
        line = line.rstrip()  # 去掉每行尾端的換行符號與空白

        # 如果這一行是空字串，代表是空行，就跳過
        if not line:
            continue

        # 遇到有效內容才加行號
        n += 1

        # :02d 表示整數至少兩位，不足前面補 0
        # 例如 1 -> 01，2 -> 02
        print(f"{n:02d}. {line}", file=fout)

# 讀出加完行號的新檔案內容並印出
print("---加行號後---")
print(dst.read_text(encoding="utf-8"))