import sys

def bitcount(x: int) -> int:
    return x.bit_count()

def solve(data: str) -> str:
    parts = data.strip().split()
    if not parts:
        return ""
    n = int(parts[0])
    m = int(parts[1])
    rows = parts[2:2 + n]

    terrain = []
    for row in rows:
        mask = 0
        for j, ch in enumerate(row):
            if ch == 'P':
                mask |= 1 << j
        terrain.append(mask)

    states = []
    cnt = {}
    for mask in range(1 << m):
        if (mask & (mask << 1)) == 0 and (mask & (mask << 2)) == 0:
            states.append(mask)
            cnt[mask] = bitcount(mask)

    valid_by_row = []
    for i in range(n):
        valid = [s for s in states if (s & ~terrain[i]) == 0]
        valid_by_row.append(valid)

    dp = {(0, 0): 0}
    for i in range(n):
        new_dp = {}
        for cur in valid_by_row[i]:
            for (prev1, prev2), val in dp.items():
                if (cur & prev1) or (cur & prev2):
                    continue
                key = (cur, prev1)
                cand = val + cnt[cur]
                if cand > new_dp.get(key, -1):
                    new_dp[key] = cand
        dp = new_dp

    return str(max(dp.values(), default=0))

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
