# R04-strings-bytes.py
# 示範 bytes 與字串的差異、切片與編碼
import re

data = b"Hello World"
print(data[0:5])  # bytes 片段
print(data.startswith(b"Hello"))
print(data.split())
print(data.replace(b"Hello", b"Hello Cruel"))

raw = b"FOO:BAR,SPAM"
# re.split 也可用 bytes pattern
print(re.split(b':|,', raw))

a = "Hello"  # str
b = b"Hello" # bytes
print(a[0])    # 取出字元 (str) -> 單字元字串
print(b[0])    # 取出 byte 值 (int)

formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # bytes encoded
