import sys

def solve_case(n: int, banned_positions: list[list[int]]) -> list[str]:
    banned = [set(x) for x in banned_positions]
    used = [False] * n
    perm = [''] * n
    results: list[str] = []
    prev: str | None = None

    def dfs(pos: int) -> None:
        nonlocal prev
        if pos == n:
            cur = ''.join(perm)
            if prev is None:
                results.append(cur)
            else:
                i = 0
                while i < n and cur[i] == prev[i]:
                    i += 1
                results.append(cur[i:])
            prev = cur
            return
        for person in range(n):
            if used[person] or (pos + 1) in banned[person]:
                continue
            used[person] = True
            perm[pos] = chr(ord('A') + person)
            dfs(pos + 1)
            used[person] = False

    dfs(0)
    return results

def parse_input(data: str) -> list[tuple[int, list[list[int]]]]:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    idx = 0
    cases = []
    while idx < len(lines):
        n = int(lines[idx])
        idx += 1
        banned_positions = []
        for _ in range(n):
            arr = list(map(int, lines[idx].split()))
            idx += 1
            banned_positions.append(arr[:-1])
        cases.append((n, banned_positions))
    return cases

def solve(data: str) -> str:
    return '\n\n'.join('\n'.join(solve_case(n, banned)) for n, banned in parse_input(data))

if __name__ == '__main__':
    print(solve(sys.stdin.read()), end='')
