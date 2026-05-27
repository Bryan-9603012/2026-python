import sys

def ok(values):
    i, j = 0, len(values) - 1
    while i <= j:
        if values[i] < 0 or values[j] < 0 or values[i] != values[j]:
            return False
        i += 1
        j -= 1
    return True

def solve(data):
    tokens = data.replace("=", " ").split()
    if not tokens:
        return ""
    t = int(tokens[0])
    idx = 1
    out = []
    for case_id in range(1, t + 1):
        if tokens[idx] == "N":
            idx += 1
        n = int(tokens[idx])
        idx += 1
        values = list(map(int, tokens[idx:idx + n * n]))
        idx += n * n
        result = "Symmetric." if ok(values) else "Non-symmetric."
        out.append(f"Test #{case_id}: {result}")
    return "\n".join(out)

print(solve(sys.stdin.read()))
