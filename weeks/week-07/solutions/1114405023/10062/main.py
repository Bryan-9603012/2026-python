import sys

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def kth(self, k: int) -> int:
        idx = 0
        bitmask = 1 << (self.n.bit_length())
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bitmask >>= 1
        return idx + 1

def solve(data: str) -> str:
    data = data.strip().split()
    if not data:
        return ""
    n = int(data[0])
    smaller_before = [0] * (n + 1)
    for i in range(2, n + 1):
        smaller_before[i] = int(data[i - 1])

    fw = Fenwick(n)
    for i in range(1, n + 1):
        fw.add(i, 1)

    ans = [0] * (n + 1)
    for pos in range(n, 0, -1):
        rank = smaller_before[pos] + 1
        value = fw.kth(rank)
        ans[pos] = value
        fw.add(value, -1)

    return "\n".join(map(str, ans[1:]))

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
