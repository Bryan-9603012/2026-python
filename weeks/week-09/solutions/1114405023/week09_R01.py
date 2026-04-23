# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數

from pathlib import Path  # Path 物件可用來更方便地操作檔案路徑

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 寫入文字檔：
# mode='wt' 表示「以文字模式寫入」
# w = write，若檔案已存在會覆蓋
# t = text，文字模式（其實預設就是文字模式）
# encoding 一定要指定，避免中文亂碼
path = Path("hello.txt")

with open(path, "wt", encoding="utf-8") as f:
    f.write("你好，Python\n")  # 寫入第一行
    f.write("第二行\n")        # 寫入第二行

# 讀回檔案內容：一次全部讀完
# 適合小檔案，不適合很大的檔案
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())  # 讀出整個檔案內容並印出

# 再讀一次：逐行讀取
# 這種方式比較適合大檔案，因為不需要一次把全部內容載入記憶體
with open(path, "rt", encoding="utf-8") as f:
    for line in f:          # 逐行迭代檔案內容
        print(line.rstrip())  # rstrip() 去掉每行結尾的換行符號

# ── 5.2 print 導向檔案 ─────────────────────────────────
# print() 不只能印到畫面，也可以用 file= 指定輸出到檔案
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)          # 將文字寫入 log.txt
    print("使用者:", "alice", file=f)  # 多個參數會自動用空白隔開

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
fruits = ["apple", "banana", "cherry"]

# sep="," 表示每個值之間用逗號分隔
# end="\n" 表示結尾加換行
# *fruits 代表把串列內容拆開成多個參數傳給 print()
with open("fruits.csv", "wt", encoding="utf-8") as f:
    print(*fruits, sep=",", end="\n", file=f)

# 追加內容到原本檔案：
# mode='at' 表示 append text，文字模式追加
with open("fruits.csv", "at", encoding="utf-8") as f:
    print("date", end=",", file=f)   # end="" 可控制不要自動換行，這裡改成逗號
    print("2026-04-23", file=f)      # 接著把日期接在同一行後面

# 直接用 Path 讀取整個文字檔內容並印出
print(Path("fruits.csv").read_text(encoding="utf-8"))

# 預期輸出：
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 'wt' 只能寫入 str（字串）
# 'wb' 只能寫入 bytes（位元組資料）
# 如果模式和資料型別不對，就會出現 TypeError

try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # 錯誤示範：文字模式不能寫入 bytes
except TypeError as e:
    print("錯誤示範:", e)  # 捕捉並印出錯誤訊息