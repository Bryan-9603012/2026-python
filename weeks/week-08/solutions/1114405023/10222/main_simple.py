rows = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]
mp = {}
for row in rows:
    for i in range(2, len(row)):
        mp[row[i]] = row[i - 2]

try:
    while True:
        s = input()
        out = ""
        for ch in s:
            t = ch.lower()
            if t in mp:
                out += mp[t].upper() if ch.isupper() else mp[t]
            else:
                out += ch
        print(out)
except EOFError:
    pass
