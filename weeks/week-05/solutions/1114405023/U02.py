# U02. 正則表達式進階技巧（2.4–2.6）
# 主題：
# 1. 預編譯正則表達式的效能比較
# 2. 使用 sub() 搭配回呼函數進行動態替換
# 3. 替換文字時保留原本的大小寫風格

import re
import timeit
from calendar import month_abbr

# --------------------------------------------------
# 一、預編譯效能（2.4）
# --------------------------------------------------
# 這段要比較：
# 1. 每次都直接用 re.findall(...)
# 2. 先用 re.compile(...) 預編譯，再重複使用
#
# 當同一個正則表達式需要被重複使用很多次時，
# 預編譯通常會比較有效率，也讓程式碼更好維護。

# 要搜尋的文字內容
# 文字中有兩個日期，格式都是 月/日/年
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 預編譯正則表達式
# (\d+) 代表「一個或多個數字」
# 三組括號表示要把 月、日、年 分別抓出來
#
# 例如：
# 11/27/2012
# 會被分成：
# group(1) = 11
# group(2) = 27
# group(3) = 2012
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# 直接使用 re 模組的 findall()
# 每次呼叫時，Python 都需要重新處理這個正則樣式
def using_module():
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)

# 使用預編譯後的 pattern 物件來找全部符合的日期
# 因為 datepat 已經先編譯好，所以重複使用時通常較快
def using_compiled():
    return datepat.findall(text)

# 使用 timeit 來測量執行時間
# number=50_000 代表每個函式執行 50,000 次
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)

# 印出兩種方法的效能比較
# 通常「預編譯」版本會稍快
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")


# --------------------------------------------------
# 二、sub 回呼函數（2.5）
# --------------------------------------------------
# re.sub() 不只能用固定字串替換，
# 也可以傳入「函式」作為第二個參數。
#
# 這樣每找到一個匹配結果，就會呼叫一次函式，
# 讓你根據匹配內容動態決定要替換成什麼。

# m: re.Match 表示一個匹配到的結果物件
# 例如匹配到 "11/27/2012" 時：
# m.group(1) -> "11"
# m.group(2) -> "27"
# m.group(3) -> "2012"
def change_date(m: re.Match) -> str:
    # month_abbr 是 calendar 模組提供的月份縮寫表
    # 例如：
    # month_abbr[1] = 'Jan'
    # month_abbr[11] = 'Nov'
    #
    # 這裡把 group(1) 的月份數字轉成整數，
    # 再查出對應的英文縮寫月份
    mon_name = month_abbr[int(m.group(1))]

    # 把原本的 月/日/年 格式
    # 改成 日 月份縮寫 年
    #
    # 例如：
    # 11/27/2012 -> 27 Nov 2012
    return f"{m.group(2)} {mon_name} {m.group(3)}"

# 使用預編譯的 datepat 進行替換
# 只要找到符合日期格式的地方，就呼叫 change_date() 來產生新字串
print(datepat.sub(change_date, text))
# 預期輸出：
# Today is 27 Nov 2012. PyCon starts 13 Mar 2013.


# --------------------------------------------------
# 三、保持大小寫一致的替換（2.6）
# --------------------------------------------------
# 有時候我們想替換單字，但又希望替換後的結果
# 保留原文字的大小寫風格。
#
# 例如：
# PYTHON -> SNAKE
# python -> snake
# Python -> Snake
#
# 這樣會讓替換結果更自然。

# matchcase(word) 會回傳一個 replace 函式
# 這是一個「閉包（closure）」寫法：
# 外層接收要替換成的新字 word
# 內層真正處理每次匹配到的內容
def matchcase(word: str):

    # 這個函式會被 re.sub() 在每次匹配成功時呼叫
    def replace(m: re.Match) -> str:
        # 取得原本匹配到的文字
        # 例如可能是 "PYTHON"、"python"、"Python"
        t = m.group()

        # 如果原文字全部都是大寫
        # 例如 PYTHON -> SNAKE
        if t.isupper():
            return word.upper()

        # 如果原文字全部都是小寫
        # 例如 python -> snake
        if t.islower():
            return word.lower()

        # 如果原文字是首字大寫
        # 例如 Python -> Snake
        if t[0].isupper():
            return word.capitalize()

        # 其他特殊情況，就直接回傳原始 word
        # 例如大小寫混合但不符合前面規則的狀況
        return word

    # 回傳這個內部函式給 re.sub() 使用
    return replace

# 原始字串中有三種不同大小寫風格的 Python
s = "UPPER PYTHON, lower python, Mixed Python"

# re.sub(..., flags=re.IGNORECASE)
# 表示搜尋時忽略大小寫，所以：
# python / PYTHON / Python 都能匹配到
#
# 但替換時不會直接用固定字串 "snake"
# 而是呼叫 matchcase("snake") 回傳的 replace 函式，
# 依照原文字風格決定替換結果
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 預期輸出：
# UPPER SNAKE, lower snake, Mixed Snake