import re

data = b"Hello Word"
print(data[0:5])
print(data.startswith(b"Hello"))
print(data.split())
print(data.replace(b"Hello",b"World Cruel"))


raw = b"Foo:BAR,SPAM"
print(re.split(rb"[:,]",raw))

a = "Hello"
b = b"Hello"
print(a[0])
print(b[0])

formatted = "{:10s} {:10d}".format("ACME",100).encode("ascii")
print(formatted)