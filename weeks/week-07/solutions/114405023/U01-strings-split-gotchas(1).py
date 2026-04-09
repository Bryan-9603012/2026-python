

import re


line = "asdf fjdk; afed, fjek,asdf, foo"
fields = re.split(r"(;|,|\s)\s*", line)
values = fields[::2]
delimiters = fields[1::2] + [""]
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)


url = "http://www.python.org"
choices = ["http:", "ftp:"]
try:
    url.startswith(choices)
except TypeError as e:
    print(f"TypeError: {e}")
print(url.startswith(tuple(choices)))


s = "  hello     world  "
print(repr(s.strip()))
print(repr(s.replace(" ", "")))
print(repr(re.sub(r"\s+", " ", s.strip())))


lines = ["  apple  \n", "  banana  \n"]
for line in (l.strip() for l in lines):
    print(line)
