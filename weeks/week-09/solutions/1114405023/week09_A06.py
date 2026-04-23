# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# gzip.open() 的用法和一般 open() 很像，
# 只是它讀寫的是 gzip 壓縮格式的檔案（通常副檔名 .gz）

# 寫入 .gz 壓縮文字檔
# 文字模式 'wt' 要記得指定 encoding，否則中文可能出問題
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回 .gz 壓縮文字檔
# 這裡用 'rt' 文字模式讀取，並逐行迭代內容
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print("gz:", line.rstrip())  # 去掉尾端換行再印出

# gzip 也能處理二進位資料
# 例如壓縮原始位元組資料，就要用 'wb' / 'rb'
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

# 顯示壓縮檔的實際檔案大小（單位：bytes）
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# 場景：
# 有時只想做暫時測試，不想在專案資料夾留下雜亂檔案，
# 這時可以用 tempfile 建立臨時資料夾或臨時檔案。

with tempfile.TemporaryDirectory() as tmp:
    # TemporaryDirectory() 會回傳一個暫存資料夾路徑字串
    # 這裡把它轉成 Path 物件，方便後續操作
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在臨時資料夾裡建立兩個文字檔
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出暫存資料夾中的內容
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 區塊後，TemporaryDirectory 會自動把整個資料夾刪掉
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔案：NamedTemporaryFile
# delete=False 表示離開 with 後不要自動刪除，方便後續自己操作
# suffix=".log" 表示這個臨時檔副檔名為 .log
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name  # 記住這個臨時檔的位置

print("暫存檔位置:", log_path)

# 用完後手動刪掉這個臨時檔
Path(log_path).unlink()

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# pickle 可以把 Python 物件直接序列化存成檔案，
# 之後再讀回來，還原成原本的 Python 物件。
#
# 適用：
# - dict
# - list
# - tuple
# - set
# - 某些自訂類別物件
#
# 不適合：
# - 跨語言交換資料（其他語言通常看不懂 pickle）
# - 長期保存資料（結構改版或 Python 版本差異可能有問題）
# 若要更穩定、可讀性更高，通常會優先考慮 json

scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 處理的是 bytes，不是文字
# 所以一定要用 'wb'（write binary）與 'rb'（read binary）

# 把 scores 字典序列化後存到 scores.pkl
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

# 從 scores.pkl 讀回物件
with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

# 驗證讀回來的內容
print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True：型別還是 dict
print("內容相等?", loaded == scores)              # True：內容和原本相同
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：
# pickle.load() 不只是讀資料，它有能力在還原物件時執行某些內嵌指令。
# 所以絕對不要載入來源不明的 .pkl 檔，否則可能有安全風險。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）