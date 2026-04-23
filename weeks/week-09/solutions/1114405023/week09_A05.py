# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 規則：
# 1. 每天只能建立一次日記檔
# 2. 如果同一天重複執行，不能覆蓋原本內容
# 3. 要提示使用者今天的日記已存在

# 取得今天日期，格式會是 YYYY-MM-DD
# 例如：2026-04-23
today = date.today().isoformat()

# 用今天日期組成檔名
diary = Path(f"diary-{today}.txt")

try:
    # 'x' 模式 = exclusive create（僅在檔案不存在時建立）
    # 如果檔案已存在，會直接丟出 FileExistsError
    with open(diary, "x", encoding="utf-8") as f:
        f.write(f"# {today} 日記\n")   # 寫入標題
        f.write("今天學了檔案 I/O。\n")  # 寫入內容

    # 如果成功建立，就印出提示訊息
    print(f"已建立 {diary}")

except FileExistsError:
    # 如果今天的日記已經存在，就不覆蓋，保留原內容
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 目標：
# 1. 遞迴走訪指定資料夾中的所有 .py 檔
# 2. 計算總行數
# 3. 計算非空白行數
# 4. 計算以 def 開頭的函式定義行數

def count_py(folder: Path):
    # total：總行數
    # nonblank：非空白行數
    # defs：以 def 開頭的行數
    total, nonblank, defs = 0, 0, 0

    # rglob("*.py")：遞迴搜尋資料夾內所有 .py 檔
    for p in folder.rglob("*.py"):

        # 以文字模式讀取 Python 檔
        # errors="replace" 表示如果遇到不能正常解碼的字元，就用替代符號取代
        # 這樣可以避免因為單一檔案編碼問題讓整個程式中斷
        with open(p, "rt", encoding="utf-8", errors="replace") as f:

            # 逐行讀取檔案內容
            for line in f:
                total += 1  # 每讀到一行，總行數加 1

                # strip() 去掉前後空白與換行
                s = line.strip()

                # 如果這行不是空字串，代表它不是空白行
                if s:
                    nonblank += 1

                # 如果去掉空白後，該行是以 "def " 開頭
                # 代表這一行可能是函式定義
                if s.startswith("def "):
                    defs += 1

    # 回傳統計結果
    return total, nonblank, defs

# 指定要統計的目錄
# 這裡是從目前位置往上兩層，再進到 week-04/in-class
target = Path("..") / ".." / "week-04" / "in-class"

# 如果目錄存在才進行統計
if target.exists():
    total, nonblank, defs = count_py(target)

    # 印出統計結果
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 若示範目錄不存在，就顯示提示
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。