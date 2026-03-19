# R02-strings-regex.py
# 示範正規表達式搜索、匹配、替換與旗標
import re

text = "Today is 11/27/2020. PyCon starts 3/13/2020."
# 使用 compile 先建立 regex 模式，可重複使用
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# findall 取得所有符合模式的 tuple 列表
print(datepat.findall(text))

m = datepat.match("11/27/2020")
assert m is not None
# groups 取出捕獲群組，group(0) 取整個匹配字串
print(m.groups(0), m.group())

for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f'Month: {month}, Day: {day}, Year: {year}')

# re.sub 取代格式 mm/dd/yyyy -> yyyy-mm-dd
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# 使用命名群組，可用 \\g<name> 方式引用
print(re.sub(r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text))

newtext, n = re.subn(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(f"替換了{n}次")

s = 'UPPER PYTHON, lower python, Mixed Python'
# IGNORECASE 忽略大小寫
print(re.findall('python', s, flags=re.IGNORECASE))

text2 = 'Computer says "no." Phone says "yes."'
# 非貪婪匹配，提取引號內內容
print(re.compile(r'"(.*?)"').findall(text2))
# 貪婪匹配，可能跨越多個引號
print(re.compile(r'"(.*)"').findall(text2))

code = "/* this is a\nmultiline comment */"
# DOTALL 讓 . 同時匹配換行
print(re.compile(r'/\*(.*?)\*/', re.DOTALL).findall(code))