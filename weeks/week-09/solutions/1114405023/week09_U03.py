# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 非文字檔（例如圖片、壓縮檔、音訊、影片、pickle）要用二進位模式處理
# 這裡先手動建立一個「假 PNG 檔」，只寫入 PNG 檔案開頭的 8 個位元組（magic number）
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

# write_bytes() 直接把 bytes 寫進檔案，不需要 encoding
Path("fake.png").write_bytes(magic)

# 用 'rb' 模式讀取二進位檔案
# r = read，b = binary（二進位）
with open("fake.png", "rb") as f:
    head = f.read(8)  # 讀前 8 個位元組

# 印出讀到的 bytes 內容
print(head)           # b'\x89PNG\r\n\x1a\n'

# 檢查讀到的內容是否和原本寫入的 magic 完全相同
print(head == magic)  # True

# bytes 可以逐一走訪，每次取出的是整數 int，不是字串 str
# 例如 b'AB' 取出來會是 65、66
for b in head[:4]:
    print(b, hex(b))  # 同時印出十進位與十六進位

# ── 文字 vs 位元組的型別差 ─────────────────────────────
# Python 的文字型別是 str
s = "你好"

# encode()：把字串依指定編碼轉成 bytes
b = s.encode("utf-8")   # str → bytes

print(s, type(s))       # 顯示原始字串與型別：<class 'str'>
print(b, type(b))       # 顯示編碼後結果與型別：<class 'bytes'>

# decode()：把 bytes 依指定編碼解回字串
print(b.decode("utf-8"))  # bytes → str

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# 寫文字檔時應明確指定 encoding，避免不同電腦預設編碼不同造成亂碼
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常情況：用 utf-8 寫入，就用 utf-8 讀取
print(Path("zh.txt").read_text(encoding="utf-8"))

# 故意示範錯誤：
# 這個檔案明明是 utf-8，卻硬要用 big5 去解碼
# 很可能會發生 UnicodeDecodeError
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    print("解碼錯誤:", e)

# 小結：
# - 文字檔：用 'rt' / 'wt'，而且建議一律明示 encoding='utf-8'
# - 非文字檔（png / zip / pickle / pdf ...）：用 'rb' / 'wb'，不需要 encoding