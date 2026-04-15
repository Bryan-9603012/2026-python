import sys

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

def decode(s: str) -> str:
    ans = []
    for ch in s:
        low = ch.lower()
        if low in mp:
            new_ch = mp[low]
            if ch.isupper():
                new_ch = new_ch.upper()
            ans.append(new_ch)
        else:
            ans.append(ch)
    return "".join(ans)

def solve(data: str) -> str:
    return "\n".join(decode(line) for line in data.splitlines())

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
