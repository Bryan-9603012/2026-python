# R03-strings-format.py
# 示範字串清理、對齊、拼接、格式化與換行包裹
import textwrap

s = "hello world \n"
# strip 會去除左右空白與換行
print(repr(s.strip()))
# lstrip 只移除左側空白
print(repr(s.lstrip()))
# 指定字符集移除前後出現的符號
print("-----hello=====".strip("-="))

text = "Hello World"
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20,"*"))
print(format(text, "^20"))
print(format(1.2345,">10.2f"))

parts = ["Is","Chicago","Not","Chicago?"]
print(" ".join(parts))
print(",".join(parts))

data = ["Acme", 50, 91.1]
print(",".join(str(d) for d in data))

name , n = "Guido",37
s = "{name} has {n} messages."
print(s.format(name=name, n=n))
print(s.format_map(vars()))
print(f"{name} has {n} messages.")

long_s = ("Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under.")
print(textwrap.fill(long_s,40))
print(textwrap.fill(long_s, 40, initial_indent="    "))